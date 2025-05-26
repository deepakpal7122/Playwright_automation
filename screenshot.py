from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()    # context can store multiple pages value that's why we using this line code 
    page.goto("https://automationtesting.in/")

    # only take front display image 
    page.screenshot(path="screenshot.png")

    # Full page screenshot
    page.wait_for_timeout(3000)
    page.screenshot(path="screenshot_fullpage.png", full_page=True)
    