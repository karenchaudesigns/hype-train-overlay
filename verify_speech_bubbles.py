from playwright.sync_api import sync_playwright
import os

def run_cuj(page):
    page.goto("http://localhost:8080/index.html")
    page.wait_for_timeout(500)

    # Click start hype train
    page.get_by_text("🚂 Start Hype Train").click()

    # Wait to see the bubble which says "The hype train is arriving..."
    page.wait_for_timeout(500)
    page.screenshot(path="/home/jules/verification/screenshots/bubble_1.png")

    # Force a teleport / boundary hit manually by executing JS if possible,
    # or just let it run for a bit. The starting pos is x=0, so the bubble at
    # start should already be clamped! Let's wait a bit and take another screenshot.
    page.wait_for_timeout(2000)
    page.screenshot(path="/home/jules/verification/screenshots/bubble_2.png")

    # Evaluate JS to spawn a bubble right on the edge to verify clamping
    page.evaluate("""
        bubbles.push({
            px: 0,
            py: 0,
            text: "Edge Test 0,0",
            spawnTime: Date.now(),
            scale: 2.0
        });
        bubbles.push({
            px: window.innerWidth,
            py: window.innerHeight,
            text: "Edge Test Max,Max",
            spawnTime: Date.now(),
            scale: 2.0
        });
    """)
    page.wait_for_timeout(500)
    page.screenshot(path="/home/jules/verification/screenshots/verification.png")
    page.wait_for_timeout(1000)

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
