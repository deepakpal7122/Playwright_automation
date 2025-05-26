from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")

    '''
    # -------- this is selenium approce ---------------

    # find the dropdown location
    selectdropdown = page.query_selector('//select[@id="Skills"]')

    # find the dropdown option
    selectdropdown.select_option(label='Backup Management')
    page.wait_for_timeout(3000)
    '''


    # ----------- New PlayWright approce -------------
    # script - commond(all_dropdown_value, click_value_name_only)
    page.select_option('//select[@id="Skills"]', label='Configuration')
    page.wait_for_timeout(3000)


    page.select_option('//select[@id="Skills"]', label='Installation')
    page.wait_for_timeout(3000)

