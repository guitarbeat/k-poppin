<script lang="ts">
	import type { UserStats } from '../types/game';

	export let game: UserStats;
	export let comments: string[];
</script>

<div class="game-result">
	<h2>Game Over!</h2>
	{#if game.gotCorrect}
		<p class="success">🎉 Congratulations! You got it in {game.score} tries!</p>
		<p class="comment">{comments[game.score - 1] || comments[comments.length - 1]}</p>
	{:else}
		<p class="failure">😔 Better luck next time!</p>
		<p class="answer">The answer was: {game.correctAnswer}</p>
	{/if}
	
	<div class="stats">
		<h3>Your Guesses:</h3>
		{#each game.guessList as guess, index}
			<div class="guess {guess.isCorrect ? 'correct' : guess.isSkipped ? 'skipped' : 'incorrect'}">
				{index + 1}. {guess.isSkipped ? 'Skipped' : guess.answer}
				{#if guess.isCorrect} ✅{:else if guess.isSkipped} ⏭️{:else} ❌{/if}
			</div>
		{/each}
	</div>
</div>

<style>
	.game-result {
		text-align: center;
		margin: 2rem 0;
		padding: 2rem;
		border: 1px solid #ccc;
		border-radius: 8px;
		background: #f8f9fa;
	}

	.success {
		color: #28a745;
		font-weight: bold;
		font-size: 1.2rem;
	}

	.failure {
		color: #dc3545;
		font-weight: bold;
		font-size: 1.2rem;
	}

	.comment {
		color: #6c757d;
		font-style: italic;
	}

	.answer {
		color: #007bff;
		font-weight: bold;
	}

	.stats {
		margin-top: 2rem;
		text-align: left;
	}

	.guess {
		padding: 0.5rem;
		margin: 0.25rem 0;
		border-radius: 4px;
	}

	.guess.correct {
		background: #d4edda;
		color: #155724;
	}

	.guess.incorrect {
		background: #f8d7da;
		color: #721c24;
	}

	.guess.skipped {
		background: #e2e3e5;
		color: #383d41;
	}
</style>