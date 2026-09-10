import os
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("http://localhost:8000/index.html")
    page.wait_for_selector("h1", timeout=5000)

    try:
        play_btn = page.get_by_role("button", name="Play")
        if play_btn.is_visible(timeout=5000):
            print("Closing Help Modal...")
            play_btn.click()
    except Exception as e:
        print(f"Error closing modal: {e}")

    page.wait_for_timeout(1000)

    # Let's wait for soundcloud iframe to load and then click the play button or wait
    try:
        print("Waiting for player...")
        # The element with text 'Turn up the volume' shows up when ready
        page.wait_for_selector("text=Turn up the volume", timeout=10000)
        print("Player ready!")
        page.screenshot(path="test_playwright.png")
        print("Page HTML:")
        print(page.inner_html("body"))
    except Exception as e:
        print(f"Error waiting for player: {e}")

    browser.close()
