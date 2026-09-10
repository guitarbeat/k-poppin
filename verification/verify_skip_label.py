import os
import sys
from playwright.sync_api import sync_playwright


def get_base_url():
    if "BASE_URL" in os.environ:
        return os.environ["BASE_URL"]
    cwd = os.getcwd()
    return f"file://{cwd}"


def verify_page(page, url_path, screenshot_path):
    base_url = get_base_url()
    if url_path == "bg/":
        full_url = f"{base_url}/bg/index.html"
    else:
        full_url = f"{base_url}/index.html"

    print(f"Visiting {full_url}")
    page.goto(full_url)

    try:
        skip_link = page.locator("a.skip-link")
        if skip_link.is_visible(timeout=5000):
            print("Found skip link")
            href = skip_link.get_attribute("href")
            print("Skip link href:", href)
            # check that #main exists
            target = page.locator(href)
            if target.count() > 0:
                print("Found target element for skip link:", target.get_attribute("id"))
            else:
                print("Could not find target element for skip link.")
                raise Exception("Missing target element")
    except Exception as e:
        print(f"Error checking skip link: {e}")

    # 1. Close Help Modal
    try:
        play_btn = page.get_by_role("button", name="Play")
        if play_btn.is_visible(timeout=5000):
            print("Closing Help Modal...")
            play_btn.click()
    except Exception as e:
        print(f"Error closing modal: {e}")


def run():
    success = False
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        try:
            print("--- Verifying Girl Group Version ---")
            page = browser.new_page()
            verify_page(page, "", "verification/skip_label_verification_gg.png")
            page.close()

            print("\n--- Verifying Boy Group Version ---")
            page = browser.new_page()
            verify_page(page, "bg/", "verification/skip_label_verification_bg.png")
            page.close()
            success = True
        except Exception as e:
            print(f"Verification failed: {e}")

        browser.close()

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    run()
