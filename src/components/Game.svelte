<script lang="ts">
	import { onMount } from 'svelte';
	import { gameState, gameConfig, userStats, currentGame, modalState, gameComments, initializeUserStats, saveUserStats, getCurrentDay } from '../stores/game';
	import { getCurrentSong } from '../lib/songs';
	import type { UserStats, Guess } from '../types/game';
	import AudioPlayer from './AudioPlayer.svelte';
	import GuessInput from './GuessInput.svelte';
	import GameResult from './GameResult.svelte';
	import Modal from './Modal.svelte';

	let currentDay: number;
	let currentSong: any;
	let userStatsList: UserStats[];
	let currentUserGame: UserStats | null = null;
	let windowHeight: number = 0;

	// Subscribe to stores
	$: gameStateValue = $gameState;
	$: modalStateValue = $modalState;

	onMount(() => {
		// Initialize
		currentDay = getCurrentDay();
		currentSong = getCurrentSong();
		
		// Initialize user stats
		initializeUserStats();
		
		// Set up current game
		setupCurrentGame();
		
		// Set up window height
		updateWindowHeight();
		window.addEventListener('resize', updateWindowHeight);
		
		// Show help modal for first time users
		if (!localStorage.getItem('firstTime')) {
			showModal('help', 'How to Play');
			localStorage.setItem('firstTime', 'false');
		}

		return () => {
			window.removeEventListener('resize', updateWindowHeight);
		};
	});

	function updateWindowHeight() {
		windowHeight = window.innerHeight;
	}

	function setupCurrentGame() {
		const stored = localStorage.getItem('userStats');
		if (stored) {
			userStatsList = JSON.parse(stored);
		} else {
			userStatsList = [];
		}

		// Find or create current game
		currentUserGame = userStatsList.find(game => game.id === currentDay.toString());
		if (!currentUserGame) {
			currentUserGame = {
				id: currentDay.toString(),
				hasStarted: false,
				hasFinished: false,
				gotCorrect: false,
				score: 0,
				guessList: []
			};
			userStatsList.push(currentUserGame);
			saveUserStats(userStatsList);
		}

		currentGame.set(currentUserGame);
	}

	function showModal(name: string, title: string, hasFrame = true) {
		modalState.set({
			isActive: true,
			hasFrame,
			title,
			name
		});
	}

	function hideModal() {
		modalState.set({
			isActive: false,
			hasFrame: true,
			title: '',
			name: ''
		});
	}

	function handleSongLoaded(event: CustomEvent) {
		const song = event.detail.currentSong;
		if (currentUserGame && currentSong) {
			currentUserGame.correctAnswer = currentSong.answer;
			currentUserGame.artist = currentSong.answer.split(' - ')[1];
			currentUserGame.title = currentSong.answer.split(' - ')[0];
			currentUserGame.img = song.artwork_url;
			currentUserGame.duration = song.duration;
			currentUserGame.genre = song.genre;
			currentUserGame.date = song.release_date;
		}
		
		gameState.update(state => ({ ...state, playerIsReady: true }));
		
		if (!currentUserGame?.hasFinished) {
			gameState.update(state => ({ ...state, gameIsActive: true }));
		}
	}

	function handlePlayStateChange(event: CustomEvent) {
		gameState.update(state => ({ 
			...state, 
			musicIsPlaying: event.detail.musicIsPlaying 
		}));
		
		if (!currentUserGame?.hasStarted) {
			currentUserGame.hasStarted = true;
			saveUserStats(userStatsList);
		}
	}

	function handleGuess(event: CustomEvent) {
		const { guess, isSkipped } = event.detail;
		const isCorrect = !isSkipped && guess === currentUserGame?.correctAnswer;
		
		// Add guess to list
		const newGuess: Guess = {
			answer: guess,
			isCorrect,
			isSkipped
		};
		
		if (currentUserGame) {
			currentUserGame.guessList = [...currentUserGame.guessList, newGuess];
			saveUserStats(userStatsList);
		}

		// Check if game is over
		if (isCorrect || currentUserGame?.guessList.length === gameConfig.maxAttempts) {
			gameState.update(state => ({ ...state, gameIsActive: false }));
			
			if (currentUserGame) {
				currentUserGame.hasFinished = true;
				currentUserGame.gotCorrect = isCorrect;
				currentUserGame.score = currentUserGame.guessList.length;
				saveUserStats(userStatsList);
			}
		}
	}
</script>

<main class="min-h-screen bg-custom-background text-custom-text">
	<div class="container mx-auto px-4 py-8" style="min-height: {windowHeight}px;">
		<!-- Game Header -->
		<header class="text-center mb-8">
			<h1 class="text-4xl font-bold mb-2">K-Pop Girl Group Heardle</h1>
			<p class="text-custom-line">Guess the K-Pop Girl Group song from the intro</p>
		</header>

		<!-- Audio Player -->
		{#if currentSong}
			<AudioPlayer 
				song={currentSong}
				on:songLoaded={handleSongLoaded}
				on:playStateChange={handlePlayStateChange}
			/>
		{/if}

		<!-- Guess Input -->
		{#if gameStateValue.gameIsActive}
			<GuessInput 
				on:guess={handleGuess}
				maxAttempts={gameConfig.maxAttempts}
				currentAttempts={currentUserGame?.guessList.length || 0}
			/>
		{/if}

		<!-- Game Result -->
		{#if currentUserGame?.hasFinished}
			<GameResult 
				game={currentUserGame}
				comments={gameComments}
			/>
		{/if}

		<!-- Modal -->
		{#if modalStateValue.isActive}
			<Modal 
				name={modalStateValue.name}
				title={modalStateValue.title}
				hasFrame={modalStateValue.hasFrame}
				on:close={hideModal}
			/>
		{/if}
	</div>
</main>

<style>
	:global(body) {
		margin: 0;
		padding: 0;
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
	}
</style>