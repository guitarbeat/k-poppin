export interface Song {
	url: string;
	answer: string;
}

export interface GameConfig {
	attemptInterval: number;
	attemptIntervalAlt: number[];
	maxAttempts: number;
	startDate: string;
}

export interface GameState {
	gameIsActive: boolean;
	musicIsPlaying: boolean;
	playerIsReady: boolean;
	isPrime: boolean;
}

export interface Guess {
	answer: string;
	isCorrect: boolean;
	isSkipped: boolean;
}

export interface UserStats {
	id: string;
	hasStarted: boolean;
	hasFinished: boolean;
	gotCorrect: boolean;
	score: number;
	guessList: Guess[];
	correctAnswer?: string;
	artist?: string;
	title?: string;
	img?: string;
	duration?: number;
	genre?: string;
	date?: string;
}

export interface ModalState {
	isActive: boolean;
	hasFrame: boolean;
	title: string;
	name: string;
}