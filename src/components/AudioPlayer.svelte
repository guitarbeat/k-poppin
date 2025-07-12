<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	import type { Song } from '../types/game';

	export let song: Song;

	const dispatch = createEventDispatcher();

	let isPlaying = false;
	let player: any = null;

	function handlePlay() {
		isPlaying = !isPlaying;
		dispatch('playStateChange', { musicIsPlaying: isPlaying });
	}

	function handleSongLoad() {
		dispatch('songLoaded', { currentSong: { artwork_url: '', duration: 0, genre: '', release_date: '' } });
	}
</script>

<div class="audio-player">
	<button on:click={handlePlay} class="play-button">
		{isPlaying ? '⏸️' : '▶️'}
	</button>
	<button on:click={handleSongLoad} class="load-button">
		Load Song
	</button>
	<p class="song-info">{song.answer}</p>
</div>

<style>
	.audio-player {
		text-align: center;
		margin: 2rem 0;
		padding: 1rem;
		border: 1px solid #ccc;
		border-radius: 8px;
	}

	.play-button, .load-button {
		margin: 0 0.5rem;
		padding: 0.5rem 1rem;
		border: none;
		border-radius: 4px;
		background: #007bff;
		color: white;
		cursor: pointer;
	}

	.play-button:hover, .load-button:hover {
		background: #0056b3;
	}

	.song-info {
		margin-top: 1rem;
		font-weight: bold;
	}
</style>