import re

files = ['index.html', 'bg/index.html']
for file in files:
    with open(file, 'r') as f:
        content = f.read()

    # Replace the hardcoded script tag with a dynamic one based on window.GOOGLE_ANALYTICS_ID
    old_script = """    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_GA_ID_HERE"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        dataLayer.push(arguments);
      }
      gtag('js', new Date());
      gtag('config', 'YOUR_GA_ID_HERE');
    </script>"""

    new_script = """    <!-- Google Analytics -->
    <script>
      if (window.GOOGLE_ANALYTICS_ID && window.GOOGLE_ANALYTICS_ID !== 'YOUR_GA_ID_HERE') {
        const script = document.createElement('script');
        script.async = true;
        script.src = `https://www.googletagmanager.com/gtag/js?id=${window.GOOGLE_ANALYTICS_ID}`;
        document.head.appendChild(script);

        window.dataLayer = window.dataLayer || [];
        function gtag() {
          dataLayer.push(arguments);
        }
        gtag('js', new Date());
        gtag('config', window.GOOGLE_ANALYTICS_ID);
      }
    </script>"""

    content = content.replace(old_script, new_script)

    with open(file, 'w') as f:
        f.write(content)
