import os

from playwright.sync_api import sync_playwright


def verify_page(page, url_path):
    cwd = os.getcwd()
    # Handle both root and bg paths correctly for file://
    if url_path == "bg/":
        # For file protocol, we point to index.html in bg/
        full_url = f"file://{cwd}/bg/index.html"
    else:
        full_url = f"file://{cwd}/index.html"

    print(f"Visiting {full_url}")
    page.goto(full_url)

    # Disable redirect if any (handled by editing html temporarily, but we reverted it.
    # If the redirect script is active, file:// might fail or redirect to https://
    # We might need to edit html again or handle redirect.
    # The script checks protocol != https. file: != https.
    # It redirects to https + location.href.substring(protocol.length).
    # file:///path/to/index.html -> https://path/to/index.html.
    # This will fail.
    # So we MUST edit the html files again to disable the redirect script.

    # 1. Close Help Modal
    try:
        play_btn = page.get_by_role("button", name="Play")
        if play_btn.is_visible(timeout=2000):
            print("Closing Help Modal...")
            play_btn.click()
    except:
        pass

    # 2. Open Stats Modal
    stats_btn = page.get_by_role("button", name="Stats")
    stats_btn.click()

    page.wait_for_selector(".modal")

    # 4. Check for bars
    bars = page.get_by_role("img").all()
    # Filter for the stats bars (aria-label contains "wins" or "losses")
    stats_bars = [
        b
        for b in bars
        if b.get_attribute("aria-label")
        and ("wins" in b.get_attribute("aria-label") or "losses" in b.get_attribute("aria-label"))
    ]

    print(f"Found {len(stats_bars)} stats bars on {url_path}.")

    for i, bar in enumerate(stats_bars):
        label = bar.get_attribute("aria-label")
        print(f"Bar {i}: aria-label='{label}'")


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        verify_page(page, "")
        verify_page(page, "bg/")

        page.screenshot(path="verification/verification.png")
        browser.close()


if __name__ == "__main__":
    run()
