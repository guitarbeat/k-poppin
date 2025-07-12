import { writable } from 'svelte/store';
import type { GameConfig, GameState, UserStats, ModalState } from '../types/game';
import dayjs from 'dayjs';

// Game configuration
export const gameConfig: GameConfig = {
	attemptInterval: 1500,
	attemptIntervalAlt: [1000, 2000, 4000, 7000, 11000, 16000],
	maxAttempts: 6,
	startDate: '2025-04-08'
};

// Game state store
export const gameState = writable<GameState>({
	gameIsActive: false,
	musicIsPlaying: false,
	playerIsReady: false,
	isPrime: false
});

// User stats store
export const userStats = writable<UserStats[]>([]);

// Current game store
export const currentGame = writable<UserStats | null>(null);

// Modal state store
export const modalState = writable<ModalState>({
	isActive: false,
	hasFrame: true,
	title: '',
	name: ''
});

// Game comments
export const gameComments = [
	'아이고! At least you discovered a new song! 😭',
	'완벽해! You\'re a true K-pop fan! 💫',
	'대단해! Had to think twice? ⭐',
	'멋있어! It\'s called the big 3 for a reason. 💝',
	'잘했어! 4th guess for the 4th generation! 💕',
	'좋아요! Nicely done! 💗',
	'괜찮아요! Almost got exposed! 💓'
];

// Utility functions
export function getCurrentDay(): number {
	const startDate = dayjs(gameConfig.startDate);
	return dayjs().diff(startDate, 'day');
}

export function initializeUserStats(): void {
	const stored = localStorage.getItem('userStats');
	if (stored) {
		userStats.set(JSON.parse(stored));
	} else {
		userStats.set([]);
		localStorage.setItem('userStats', JSON.stringify([]));
	}
}

export function saveUserStats(stats: UserStats[]): void {
	localStorage.setItem('userStats', JSON.stringify(stats));
	userStats.set(stats);
}