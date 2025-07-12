import './app.css';
import Game from './components/Game.svelte';

const app = new Game({
	target: document.body
});

export default app;