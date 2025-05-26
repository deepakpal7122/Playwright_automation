from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    broswer = p.chromium.launch(headless=False)
    page = broswer.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


    # xpath - Relative xpath - '//' - //tagname[@attributename = "attributevalue"]
    username = page.wait_for_selector('//input[@name="username"]')
    username.type("admin")

    password = page.wait_for_selector('//input[@name="password"]')
    password.type("admin123")

    loginbutton = page.wait_for_selector('//button[@type="submit"]')
    loginbutton.click()
    page.wait_for_timeout(3000)
    

    '''
    # Using text - //tagname[text() = "text"]
    page.wait_for_selector("//p[text() = 'Forgot your password? ']").click()
    page.wait_for_timeout(3000)


    # Using contains 
    attributes = //tagname[contains(@attibute, "value")]
    text = //tagname[contains(text(), "Forget Your")]
    '''