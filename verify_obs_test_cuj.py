from playwright.sync_api import sync_playwright
import os

def run_cuj(page):
    # Go to normal obs mode
    page.goto("http://localhost:8080/index.html?obs=true")
    page.wait_for_timeout(1000)

    # Go to test mode while in OBS
    page.goto("http://localhost:8080/index.html?obs=true&test=true")
    page.wait_for_timeout(1000)

    # Press 'h' to hide the panel
    page.keyboard.press('h')
    page.wait_for_timeout(1000)

    # Press 'h' to show the panel again
    page.keyboard.press('h')
    page.wait_for_timeout(1000)

    os.makedirs("/home/jules/verification/screenshots", exist_ok=True)
    page.screenshot(path="/home/jules/verification/screenshots/verification.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(record_video_dir="/home/jules/verification/videos")
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
