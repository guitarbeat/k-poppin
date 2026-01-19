from playwright.sync_api import sync_playwright, expect
import os

def check_aria_labels():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use a mobile viewport as the app is mobile-first
        context = browser.new_context(viewport={"width": 375, "height": 667})
        page = context.new_page()

        # Load the local index.html file
        page.goto(f"file://{os.getcwd()}/index.html")

        # Wait for the main app to load (checking for h1 title)
        page.wait_for_selector("h1")

        # Close the initial Help Modal to interact with the page
        # The close button has aria-label="Close modal"
        page.get_by_role("button", name="Close modal").click()

        # Now verify the specific buttons
        # 1. Open Help modal again to check the "Play" button
        page.get_by_label("Help").click()

        # Wait for "Play" button to be visible
        play_button = page.get_by_text("Play", exact=True)
        # It's a button containing text "Play".
        # We need to check if it has an aria-label.
        # Ideally, it should NOT have an empty aria-label.

        # Get the element handle
        play_btn_element = play_button.element_handle()
        aria_label = play_btn_element.get_attribute("aria-label")

        print(f"Play Button ARIA Label: '{aria_label}'")

        if aria_label == "":
            print("FAILURE: Play button has empty aria-label")
        elif aria_label is None:
            print("SUCCESS: Play button has NO aria-label (content is accessible)")
        else:
            print(f"INFO: Play button has aria-label: {aria_label}")

        # Close help modal
        page.get_by_role("button", name="Close modal").click()

        # 2. Check "Stats" modal for "Share" button (simulate game over?)
        # Actually, let's just check the code behavior on a known button that relied on default.
        # "Stats" button itself has a label "Stats".

        stats_btn = page.get_by_role("button", name="Stats")
        stats_aria = stats_btn.get_attribute("aria-label")
        print(f"Stats Button ARIA Label: '{stats_aria}'")

        if stats_aria != "Stats":
             print(f"FAILURE: Stats button label mismatch. Expected 'Stats', got '{stats_aria}'")

        # Take a screenshot for evidence
        page.screenshot(path="verification/verification.png")

        browser.close()

if __name__ == "__main__":
    check_aria_labels()
