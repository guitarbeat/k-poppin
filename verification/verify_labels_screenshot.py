
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

        # Take a screenshot to prove we are on the page and buttons are visible
        page.screenshot(path='verification/verification.png')

        browser.close()

if __name__ == "__main__":
    verify_aria_labels()
