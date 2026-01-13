
from playwright.sync_api import sync_playwright

def verify_aria_labels():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the page directly from file since it's a static app
        import os
        pwd = os.getcwd()
        page.goto(f'file://{pwd}/index.html')

        # Wait for the app to initialize (it might need time for main.js to run)
        page.wait_for_timeout(5000)

        # Check for Skip button ARIA label
        skip_button = page.locator('button[aria-label="Skip current turn"]')
        if skip_button.count() > 0:
            print("SUCCESS: Skip button with aria-label found")
        else:
            print("FAILURE: Skip button with aria-label NOT found")
            # Debug: print all buttons with labels
            buttons = page.locator('button').all()
            for b in buttons:
                print(f"Button: {b.get_attribute('aria-label')} - Text: {b.text_content()}")

        # Check for Submit button ARIA label
        submit_button = page.locator('button[aria-label="Submit your guess"]')
        if submit_button.count() > 0:
            print("SUCCESS: Submit button with aria-label found")
        else:
            print("FAILURE: Submit button with aria-label NOT found")

        browser.close()

if __name__ == "__main__":
    verify_aria_labels()
