import os
from playwright.sync_api import sync_playwright, expect

def verify_clear_search_accessibility(page):
    # Navigate to the local file
    file_path = os.path.abspath("index.html")
    page.goto(f"file://{file_path}")

    # Wait for the app to load
    page.wait_for_selector("h1")

    # Close the initial help modal if it appears
    try:
        # Based on previous patches, the play button in help modal has text "Play"
        play_button = page.get_by_role("button", name="Play")
        if play_button.is_visible():
            play_button.click()
    except Exception as e:
        print(f"Modal handling info: {e}")

    # Locate the search input
    search_input = page.get_by_label("Search for the song title")
    expect(search_input).to_be_visible()

    # Locate the clear search button by its new aria-label
    clear_button = page.get_by_role("button", name="Clear search")
    expect(clear_button).to_be_visible()

    # Type something to make sure clear button is relevant (though it might be visible always based on code)
    search_input.fill("test")

    # Take a screenshot of the search area
    page.screenshot(path="verification/clear_search_button.png")

    # Verify clicking it clears the input
    clear_button.click()
    expect(search_input).to_have_value("")

    print("Verification successful: Clear search button is accessible and functional.")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_clear_search_accessibility(page)
        except Exception as e:
            print(f"Verification failed: {e}")
            page.screenshot(path="verification/error.png")
        finally:
            browser.close()
