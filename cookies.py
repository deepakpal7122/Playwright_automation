from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()    # context can store multiple pages value that's why we using this line code 
    page.goto("https://demo.automationtesting.in/Windows.html")


    # Print all cookies 
    my_cookies = page.context.cookies()
    print(my_cookies)

    # clear all the cookies
    page.context.clear_cookies()

    # add new cookies
    new_cookies = { 'name' : 'Deepak',  'age' : '25' }
    page.context.add_cookies([new_cookies])
