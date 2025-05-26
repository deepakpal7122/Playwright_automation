from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    broswer = p.chromium.launch(headless=False)
    page = broswer.new_page()
    page.goto("https://demo.automationtesting.in/")

# cssselector - id - # ,  class - . , attribute - tagname[attribute = "value"] 

    # using id 
    emailtxtbox = page.wait_for_selector('#email')
    emailtxtbox.type('test@gmail.com')
    page.wait_for_timeout(3000)

    buttonlogin = page.wait_for_selector('#enterimg')
    buttonlogin.click()
    page.wait_for_timeout(3000)


# launch new Url 
with sync_playwright() as p:
    broswer = p.chromium.launch(headless=False)
    page = broswer.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # using css attribute
    username = page.wait_for_selector('input[name="username"]')
    username.type("admin")

    password = page.wait_for_selector('input[name="password"]')
    password.type("admin123")

    loginbutton = page.wait_for_selector('button[type="submit"]')
    loginbutton.click()
    page.wait_for_timeout(3000)

