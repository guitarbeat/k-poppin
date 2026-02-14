import os
import sys
from playwright.sync_api import sync_playwright


def get_base_url():
    if "BASE_URL" in os.environ:
        return os.environ["BASE_URL"]
    cwd = os.getcwd()
    return f"file://{cwd}"


def verify_page(page, url_path):
    base_url = get_base_url()
    # Handle both root and bg paths correctly
    if url_path == "bg/":
        full_url = f"{base_url}/bg/index.html"
    else:
        full_url = f"{base_url}/index.html"

    print(f"Visiting {full_url}")
    page.goto(full_url)

    # 1. Close Help Modal
    try:
        play_btn = page.get_by_role("button", name="Play")
        if play_btn.is_visible(timeout=2000):
            print("Closing Help Modal...")
            play_btn.click()
    except Exception:
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

    if len(stats_bars) == 0:
        raise Exception("No stats bars found!")


def run():
    success = False
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            verify_page(page, "")
            verify_page(page, "bg/")
            page.screenshot(path="verification/verification.png")
            success = True
        except Exception as e:
            print(f"Verification failed: {e}")

        browser.close()

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    run()
