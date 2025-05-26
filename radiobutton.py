from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")


    radio_button = page.query_selector('//input[@value="Male"]')

    # both commond is correct 
    radio_button.check()
    # radio_button.click()
    
    # checking radio button is clicked or not
    if radio_button.is_checked():
        print("Passed")
    else:
        print("Failed")

    page.wait_for_timeout(3000)