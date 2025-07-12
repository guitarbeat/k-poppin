<script lang="ts">
	import { createEventDispatcher } from 'svelte';

	export let maxAttempts: number;
	export let currentAttempts: number;

	const dispatch = createEventDispatcher();

	let guess = '';
	let isSkipped = false;

	function handleSubmit() {
		if (guess.trim()) {
			dispatch('guess', { guess: guess.trim(), isSkipped: false });
			guess = '';
		}
	}

	function handleSkip() {
		dispatch('guess', { guess: '', isSkipped: true });
	}

	function handleKeydown(event: KeyboardEvent) {
		if (event.key === 'Enter') {
			handleSubmit();
		}
	}
</script>

<div class="guess-input">
	<input
		type="text"
		bind:value={guess}
		on:keydown={handleKeydown}
		placeholder="Enter your guess..."
		disabled={currentAttempts >= maxAttempts}
		class="guess-field"
	/>
	<button on:click={handleSubmit} disabled={!guess.trim() || currentAttempts >= maxAttempts} class="submit-btn">
		Submit
	</button>
	<button on:click={handleSkip} disabled={currentAttempts >= maxAttempts} class="skip-btn">
		Skip
	</button>
	<p class="attempts">Attempts: {currentAttempts}/{maxAttempts}</p>
</div>

<style>
	.guess-input {
		text-align: center;
		margin: 2rem 0;
	}

	.guess-field {
		padding: 0.5rem;
		margin-right: 0.5rem;
		border: 1px solid #ccc;
		border-radius: 4px;
		width: 300px;
	}

	.submit-btn, .skip-btn {
		margin: 0 0.25rem;
		padding: 0.5rem 1rem;
		border: none;
		border-radius: 4px;
		cursor: pointer;
	}

	.submit-btn {
		background: #28a745;
		color: white;
	}

	.submit-btn:hover:not(:disabled) {
		background: #218838;
	}

	.skip-btn {
		background: #6c757d;
		color: white;
	}

	.skip-btn:hover:not(:disabled) {
		background: #5a6268;
	}

	.submit-btn:disabled, .skip-btn:disabled {
		opacity: 0.5;
		cursor: not-allowed;
	}

	.attempts {
		margin-top: 1rem;
		color: #666;
	}
</style>