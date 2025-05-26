from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html")


    # By default, dialogs are auto-dismissed by Playwright, so you don't have to handle them
    # that triggers the dialog to either dialog.accept() or dialog.dismiss() it.


    # By defualt it will cancel alert 
    page.wait_for_selector('//a[@href="#CancelTab"]').click()
    page.wait_for_timeout(3000)


    # this commond Bydefault it cancel alert popup autoamtically 
    '''page.wait_for_selector('//button[@class="btn btn-primary"]').click()    
    page.wait_for_timeout(3000)'''
    

    # This commond we can accept alert 
    page.on("dialog", lambda dialog: dialog.accept())
    # page.on("dialog", lambda dialog: dialog.dismiss())   # this commond will click cancel alert popup
    page.on("dialog", lambda dialog: print(dialog.message))    # this commond will print alert message
    page.wait_for_selector('//button[@class="btn btn-primary"]').click()
    page.wait_for_timeout(5000)

