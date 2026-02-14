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

    # 1. Close Help Modal
    try:
        play_btn = page.get_by_role("button", name="Play")
        if play_btn.is_visible(timeout=5000):
            print("Closing Help Modal...")
            play_btn.click()
    except Exception as e:
        print(f"Error closing modal: {e}")

    # 2. Check Skip Button Label
    try:
        page.wait_for_selector("button[aria-label^='Skip']", timeout=5000)
    except Exception:
        print("Could not find Skip button by selector.")

    buttons = page.get_by_role("button").all()
    skip_btn = None
    for btn in buttons:
        label = btn.get_attribute("aria-label")
        if label and label.startswith("Skip"):
            skip_btn = btn
            break

    if skip_btn:
        label = skip_btn.get_attribute("aria-label")
        print(f"Found Skip button with aria-label: '{label}'")
        # Check for pattern (+Xs) or (+X.Ys)
        if "(+" in label and "s)" in label:
            print("SUCCESS: Label contains time penalty.")
            # Scroll to button and screenshot
            skip_btn.scroll_into_view_if_needed()
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
        else:
            print("FAILURE: Label missing time penalty.")
            raise Exception("Label missing time penalty")
    else:
        print("FAILURE: Skip button not found.")
        raise Exception("Skip button not found")


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
