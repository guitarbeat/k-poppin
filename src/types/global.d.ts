declare global {
  interface Window {
    dataLayer: any[];
    gtag: (...args: any[]) => void;
    SC: {
      Widget: {
        new (elementId: string): SoundCloudWidget;
        Events: {
          READY: string;
          PAUSE: string;
          PLAY: string;
          PLAY_PROGRESS: string;
        };
      };
    };
  }
  
  function gtag(...args: any[]): void;
}

interface SoundCloudWidget {
  bind(event: string, callback: (data?: any) => void): void;
  getCurrentSound(callback: (sound: any) => void): void;
  seekTo(position: number): void;
  play(): void;
  pause(): void;
  toggle(): void;
}

export {};

export {};