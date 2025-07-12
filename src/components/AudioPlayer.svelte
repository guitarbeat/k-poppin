<script lang="ts">
  import { onMount, createEventDispatcher } from 'svelte';
  import type { GameState, CurrentHeardle, Config } from '../types/game';

  export let config: Config;
  export let gameState: GameState;
  export let currentHeardle: CurrentHeardle;
  export let trackDuration: number;
  export let currentAttempt: number;

  const dispatch = createEventDispatcher();

  let widget: SoundCloudWidget | null = null;
  let widgetContainer: HTMLDivElement;
  let isReady = false;
  let isBlocked = false;
  let currentPosition = 0;
  let progress = 0;
  let hasStarted = false;
  let showTimeout = false;
  let attemptInterval: number;

  onMount(() => {
    initializeWidget();
  });

  function initializeWidget() {
    // Load SoundCloud API
    const script = document.createElement('script');
    script.src = 'https://w.soundcloud.com/player/api.js';
    script.onload = createWidget;
    document.head.appendChild(script);
  }

  function createWidget() {
    const iframe = document.createElement('iframe');
    iframe.name = currentHeardle.id.toString();
    iframe.id = `soundcloud${currentHeardle.id}`;
    iframe.allow = 'autoplay';
    iframe.height = '0';
    iframe.src = `https://w.soundcloud.com/player/?url=${currentHeardle.url}&cache=${currentHeardle.id}`;
    
    widgetContainer.appendChild(iframe);
    
    // Initialize widget after a short delay
    setTimeout(() => {
      widget = new window.SC.Widget(`soundcloud${currentHeardle.id}`);
      bindEvents();
    }, 100);
  }

  function bindEvents() {
    if (!widget) return;

    widget.bind(window.SC.Widget.Events.READY, () => {
      widget.getCurrentSound((sound: any) => {
        if (sound.policy === 'BLOCK') {
          isBlocked = true;
        }
        dispatch('updateSong', { currentSong: sound });
      });

      widget.bind(window.SC.Widget.Events.PAUSE, () => {
        dispatch('updatePlayerState', { musicIsPlaying: false });
      });

      widget.bind(window.SC.Widget.Events.PLAY, () => {
        if (!hasStarted) {
          hasStarted = true;
        }
        dispatch('updatePlayerState', { musicIsPlaying: true });
      });

      widget.bind(window.SC.Widget.Events.PLAY_PROGRESS, (event: any) => {
        currentPosition = event.currentPosition;
        
        if (currentAttempt === 1) {
          if (gameState.isPrime) {
            attemptInterval = config.attemptIntervalAlt[currentAttempt - 1];
            progress = (currentPosition / attemptInterval) * 100;
            if (currentPosition > attemptInterval) {
              resetAndPlay();
            }
          } else {
            progress = (currentPosition / (currentAttempt * config.attemptInterval)) * 100;
            if (currentPosition > currentAttempt * config.attemptInterval) {
              resetAndPlay();
            }
          }
        } else {
          progress = (currentPosition / trackDuration) * 100;
          if (currentPosition > trackDuration) {
            resetAndPlay();
          }
        }
      });
    });
  }

  function play() {
    if (widget) {
      widget.seekTo(0);
      widget.play();
    }
  }

  function pause() {
    if (widget) {
      widget.pause();
    }
  }

  function resetAndPlay() {
    if (widget) {
      widget.seekTo(0);
      widget.pause();
    }
  }

  function togglePlayState() {
    if (widget) {
      widget.toggle();
    }
  }

  function formatTime(seconds: number): string {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = Math.floor(seconds % 60);
    return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
  }

  // Expose methods for parent component
  export { play, pause, resetAndPlay, togglePlayState };
</script>

<div class="audio-player">
  <div bind:this={widgetContainer} class="widget-container hidden"></div>
  
  <div class="controls">
    <button on:click={togglePlayState} class="play-button">
      {gameState.musicIsPlaying ? '⏸️' : '▶️'}
    </button>
    
    <div class="progress-container">
      <div class="progress-bar" style="width: {progress}%"></div>
    </div>
    
    <div class="time-display">
      {formatTime(currentPosition)} / {formatTime(trackDuration)}
    </div>
  </div>
  
  {#if isBlocked}
    <div class="error-message">
      Oh no! Seems like today's track is unavailable on SoundCloud in your location
    </div>
  {/if}
</div>

<style>
  .audio-player {
    padding: 1rem;
    background: rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    margin: 1rem 0;
  }

  .widget-container {
    display: none;
  }

  .hidden {
    display: none;
  }

  .controls {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .play-button {
    background: none;
    border: 2px solid white;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 50px;
    cursor: pointer;
    font-size: 1.2rem;
  }

  .play-button:hover {
    background: rgba(255, 255, 255, 0.1);
  }

  .progress-container {
    flex: 1;
    height: 4px;
    background: rgba(255, 255, 255, 0.3);
    border-radius: 2px;
    overflow: hidden;
  }

  .progress-bar {
    height: 100%;
    background: white;
    transition: width 0.1s ease;
  }

  .time-display {
    color: white;
    font-size: 0.9rem;
    min-width: 80px;
  }

  .error-message {
    color: #ff6b6b;
    text-align: center;
    margin-top: 1rem;
    padding: 1rem;
    background: rgba(255, 107, 107, 0.1);
    border-radius: 4px;
  }
</style>