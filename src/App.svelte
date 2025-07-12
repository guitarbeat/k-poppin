<script lang="ts">
  import { onMount } from 'svelte';
  import { gameState, currentHeardle, userGuesses, modalState } from './stores/game';
  import { songs } from './data/songs';
  import { config } from './config';
  import GoogleAnalytics from './components/GoogleAnalytics.svelte';
  import Header from './components/Header.svelte';
  import GameResult from './components/GameResult.svelte';
  import GameStats from './components/GameStats.svelte';
  import AudioPlayer from './components/AudioPlayer.svelte';
  import Modal from './components/Modal.svelte';
  import GuessInput from './components/GuessInput.svelte';

  let audioPlayer: AudioPlayer;
  let windowHeight = 0;

  // Initialize game state
  onMount(() => {
    initializeGame();
    updateWindowHeight();
    window.addEventListener('resize', updateWindowHeight);
    
    return () => {
      window.removeEventListener('resize', updateWindowHeight);
    };
  });

  function updateWindowHeight() {
    windowHeight = window.innerHeight;
  }

  function initializeGame() {
    const today = getDaysSinceStart();
    
    if (today >= songs.length) {
      console.log('songs', songs.length);
      console.log('day', today);
      console.log('out of songs');
      return;
    }

    const currentSong = songs[today];
    const gameData = {
      url: currentSong.url,
      correctAnswer: currentSong.answer,
      id: today,
      guessList: [],
      hasFinished: false,
      hasStarted: false,
      artist: '',
      title: '',
      img: '',
      duration: 0,
      genre: '',
      date: ''
    };

    // Load user stats from localStorage
    let userStats = [];
    const storedStats = localStorage.getItem('userStats');
    if (storedStats) {
      userStats = JSON.parse(storedStats);
    }

    let todayGame = userStats.find((game: any) => game.id === today);
    if (!todayGame) {
      todayGame = { ...gameData };
      userStats.push(todayGame);
      localStorage.setItem('userStats', JSON.stringify(userStats));
    }

    // Update stores
    currentHeardle.set(gameData);
    userGuesses.set(todayGame.guessList || []);
    gameState.set({
      gameIsActive: false,
      musicIsPlaying: false,
      playerIsReady: false,
      isPrime: today >= 7
    });

    // Show help modal for first-time users
    if (!localStorage.getItem('firstTime')) {
      modalState.set({
        isActive: true,
        name: 'help',
        title: 'how to play',
        hasFrame: true
      });
      localStorage.setItem('firstTime', 'false');
    }
  }

  function getDaysSinceStart(): number {
    const startDate = new Date(config.startDate);
    const today = new Date();
    const diffTime = today.getTime() - startDate.getTime();
    return Math.floor(diffTime / (1000 * 60 * 60 * 24));
  }

  function handleSongUpdate(event: CustomEvent) {
    const song = event.detail.currentSong;
    const currentData = $currentHeardle;
    const [title, artist] = currentData.correctAnswer.split(' - ');
    
    currentHeardle.update(data => ({
      ...data,
      artist,
      title,
      img: song.artwork_url,
      duration: song.duration,
      genre: song.genre,
      date: song.release_date
    }));

    gameState.update(state => ({
      ...state,
      playerIsReady: true
    }));

    const userStats = JSON.parse(localStorage.getItem('userStats') || '[]');
    const todayGame = userStats.find((game: any) => game.id === currentData.id);
    
    if (!todayGame?.hasFinished) {
      gameState.update(state => ({
        ...state,
        gameIsActive: true
      }));
    }
  }

  function handlePlayerStateUpdate(event: CustomEvent) {
    const { musicIsPlaying } = event.detail;
    const currentData = $currentHeardle;
    
    if (!currentData.hasStarted) {
      // Track game start
      trackEvent('startGame', { name: 'startGame' });
      trackEvent(`startGame#${currentData.id}`, { name: 'startGame' });
      
      currentHeardle.update(data => ({
        ...data,
        hasStarted: true
      }));
    }

    gameState.update(state => ({
      ...state,
      musicIsPlaying
    }));
  }

  function handleGuess(event: CustomEvent) {
    const { guess, isSkipped } = event.detail;
    const currentData = $currentHeardle;
    const isCorrect = !isSkipped && guess === currentData.correctAnswer;
    
    // Track guess
    if (isCorrect) {
      trackEvent('correctGuess', { name: 'correctGuess' });
      trackEvent(`correctGuess#${currentData.id}`, { name: 'correctGuess' });
    } else if (isSkipped) {
      trackEvent('skippedGuess', { name: 'skippedGuess' });
      trackEvent(`skippedGuess#${currentData.id}`, { name: 'skippedGuess' });
    } else {
      trackEvent('incorrectGuess', { name: 'incorrectGuess' });
      trackEvent(`incorrectGuess#${currentData.id}`, { name: 'incorrectGuess' });
    }

    // Add guess to list
    const newGuess = {
      answer: guess,
      isCorrect,
      isSkipped
    };

    userGuesses.update(guesses => [...guesses, newGuess]);

    // Update localStorage
    const userStats = JSON.parse(localStorage.getItem('userStats') || '[]');
    const todayGame = userStats.find((game: any) => game.id === currentData.id);
    if (todayGame) {
      todayGame.guessList = $userGuesses;
      localStorage.setItem('userStats', JSON.stringify(userStats));
    }

    // Check if game is over
    const currentGuesses = $userGuesses;
    if (currentGuesses.length >= config.maxAttempts || isCorrect) {
      gameState.update(state => ({
        ...state,
        gameIsActive: false
      }));

      if (todayGame) {
        todayGame.hasFinished = true;
        todayGame.gotCorrect = isCorrect;
        todayGame.score = currentGuesses.length;
        localStorage.setItem('userStats', JSON.stringify(userStats));
      }

      // Reset audio player
      if (audioPlayer) {
        audioPlayer.resetAndPlay();
      }

      // Track game end
      if (isCorrect) {
        trackEvent('wonGame', { name: 'won' });
        trackEvent(`wonGame#${currentData.id}`, { name: 'won' });
      } else {
        trackEvent('lostGame', { name: 'lost' });
        trackEvent(`lostGame#${currentData.id}`, { name: 'lost' });
      }

      trackEvent(`endGame${currentData.id}in${currentGuesses.length}`, { name: `#${currentGuesses.length}` });
      trackEvent('endGame', { name: 'endGame' });
      trackEvent(`endGame#${currentData.id}`, { name: 'endGame' });
      trackEvent(`gameStats#${currentData.id}`, { name: currentGuesses });
    }
  }

  function handleModal(event: CustomEvent) {
    const { name, title, hasFrame } = event.detail;
    modalState.set({
      isActive: true,
      name,
      title,
      hasFrame
    });
  }

  function closeModal() {
    modalState.update(state => ({
      ...state,
      isActive: false
    }));
  }

  function trackEvent(eventName: string, parameters: any) {
    // Google Analytics tracking
    if (typeof gtag !== 'undefined') {
      gtag('event', eventName, parameters);
    }
  }
</script>

<svelte:head>
  <title>K-pop Girl Group Heardle</title>
  <meta name="description" content="Guess the K-pop Girl Group song from the intro in as few tries as possible" />
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png" />
  <link rel="manifest" href="/site.webmanifest" />
</svelte:head>

<GoogleAnalytics properties={['G-VC91QPG37E']} />

<main class="bg-custom-bg text-custom-fg overflow-auto flex flex-col" style="height: {windowHeight}px">
  {#if $modalState.isActive}
    <Modal />
  {/if}

  <div class="flex-none">
    <Header on:modal={handleModal} />
  </div>

  <div class="w-full flex flex-col flex-grow relative">
    <div class="max-w-screen-sm w-full mx-auto h-full flex flex-col justify-between overflow-auto">
      <GameResult 
        userGuesses={$userGuesses}
        maxAttempts={config.maxAttempts}
        currentHeardle={$currentHeardle}
        todaysGame={JSON.parse(localStorage.getItem('userStats') || '[]').find((game: any) => game.id === $currentHeardle.id)}
      />

      <GameStats 
        {config}
        userGuesses={$userGuesses}
        currentHeardle={$currentHeardle}
        hasFinished={JSON.parse(localStorage.getItem('userStats') || '[]').find((game: any) => game.id === $currentHeardle.id)?.hasFinished}
        gotCorrect={JSON.parse(localStorage.getItem('userStats') || '[]').find((game: any) => game.id === $currentHeardle.id)?.gotCorrect}
        isPrime={$gameState.isPrime}
        guessRef={JSON.parse(localStorage.getItem('userStats') || '[]').find((game: any) => game.id === $currentHeardle.id)?.gotCorrect ? $userGuesses.length : 0}
      />
    </div>
  </div>

  <AudioPlayer 
    bind:this={audioPlayer}
    {config}
    gameState={$gameState}
    currentHeardle={$currentHeardle}
    trackDuration={$currentHeardle.duration}
    currentAttempt={$userGuesses.length + 1}
    on:updateSong={handleSongUpdate}
    on:updatePlayerState={handlePlayerStateUpdate}
  />

  {#if !JSON.parse(localStorage.getItem('userStats') || '[]').find((game: any) => game.id === $currentHeardle.id)?.hasFinished && $gameState.gameIsActive}
    <GuessInput on:guess={handleGuess} />
  {/if}
</main>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  }

  :global(.bg-custom-bg) {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  }

  :global(.text-custom-fg) {
    color: white;
  }
</style>