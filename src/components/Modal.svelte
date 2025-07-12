<script lang="ts">
	import { createEventDispatcher } from 'svelte';

	export let name: string;
	export let title: string;
	export let hasFrame: boolean = true;

	const dispatch = createEventDispatcher();

	function handleClose() {
		dispatch('close');
	}

	function handleBackdropClick(event: MouseEvent) {
		if (event.target === event.currentTarget) {
			handleClose();
		}
	}
</script>

<div class="modal-backdrop" on:click={handleBackdropClick}>
	<div class="modal {hasFrame ? 'with-frame' : ''}">
		<div class="modal-header">
			<h2>{title}</h2>
			<button class="close-btn" on:click={handleClose}>×</button>
		</div>
		<div class="modal-content">
			{#if name === 'help'}
				<div class="help-content">
					<h3>How to Play</h3>
					<ol>
						<li>Listen to the song intro</li>
						<li>Type your guess in the input field</li>
						<li>You have 6 attempts to guess correctly</li>
						<li>You can skip if you're not sure</li>
						<li>Share your results with friends!</li>
					</ol>
				</div>
			{:else}
				<p>Modal content for: {name}</p>
			{/if}
		</div>
	</div>
</div>

<style>
	.modal-backdrop {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background: rgba(0, 0, 0, 0.5);
		display: flex;
		justify-content: center;
		align-items: center;
		z-index: 1000;
	}

	.modal {
		background: white;
		border-radius: 8px;
		max-width: 500px;
		width: 90%;
		max-height: 80vh;
		overflow-y: auto;
	}

	.modal.with-frame {
		border: 2px solid #007bff;
	}

	.modal-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 1rem;
		border-bottom: 1px solid #dee2e6;
	}

	.modal-header h2 {
		margin: 0;
		font-size: 1.5rem;
	}

	.close-btn {
		background: none;
		border: none;
		font-size: 1.5rem;
		cursor: pointer;
		padding: 0;
		width: 30px;
		height: 30px;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.close-btn:hover {
		background: #f8f9fa;
		border-radius: 4px;
	}

	.modal-content {
		padding: 1rem;
	}

	.help-content ol {
		text-align: left;
		padding-left: 1.5rem;
	}

	.help-content li {
		margin: 0.5rem 0;
	}
</style>