<script lang="ts">
  import { onMount } from 'svelte';

  export let properties: string[];

  onMount(() => {
    // Initialize Google Analytics
    if (typeof window !== 'undefined' && properties.length > 0) {
      const script = document.createElement('script');
      script.async = true;
      script.src = `https://www.googletagmanager.com/gtag/js?id=${properties[0]}`;
      document.head.appendChild(script);

      window.dataLayer = window.dataLayer || [];
      function gtag(...args: any[]) {
        window.dataLayer.push(args);
      }
      gtag('js', new Date());
      gtag('config', properties[0]);

      // Make gtag globally available
      (window as any).gtag = gtag;
    }
  });
</script>

<!-- Google Analytics component - no visual output -->