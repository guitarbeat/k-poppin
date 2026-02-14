import os

from playwright.sync_api import sync_playwright


def test_load():
    cwd = os.getcwd()
    file_path = f"file://{cwd}/index.html"
    print(f"Loading {file_path}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Listen for console errors
        page.on(
            "console",
            lambda msg: print(f"CONSOLE: {msg.text}") if msg.type == "error" else None,
        )
        page.on("pageerror", lambda err: print(f"PAGE ERROR: {err}"))

        page.goto(file_path)

        # Wait for the main container or header to ensure JS executed
        # The h1 "K-Pop Girl Group Heardle" is created by JS
        try:
            page.wait_for_selector("h1", timeout=5000)
            print("Successfully found h1 element created by JS.")

            # Take screenshot
            page.screenshot(path="verification/loaded.png")
            print("Screenshot taken.")

        except Exception as e:
            print(f"Failed to load app: {e}")

        browser.close()


if __name__ == "__main__":
    test_load()
