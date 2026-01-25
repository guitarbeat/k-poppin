from playwright.sync_api import sync_playwright
import os

def test_load():
    cwd = os.getcwd()
    file_path = f"file://{cwd}/bg/index.html"
    print(f"Loading {file_path}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.on("console", lambda msg: print(f"CONSOLE: {msg.text}") if msg.type == "error" else None)
        page.on("pageerror", lambda err: print(f"PAGE ERROR: {err}"))

        page.goto(file_path)

        try:
            page.wait_for_selector("h1", timeout=5000)
            print("Successfully found h1 element created by JS in BG version.")

        except Exception as e:
            print(f"Failed to load BG app: {e}")

        browser.close()

if __name__ == "__main__":
    test_load()
