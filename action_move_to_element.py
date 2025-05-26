from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()    # context can store multiple pages value that's why we using this line code 
    page.goto("https://demo.automationtesting.in/Selectable.html")

    # Mouse Actions
    
    # Hover the dropdown
    page.wait_for_selector('//a[text() = "SwitchTo"]').hover()

    # click to element
    page.wait_for_selector('//a[text() = "SwitchTo"]').click()

    # Double click
    page.wait_for_selector('//a[text() = "SwitchTo"]').dblclick()

    # Right click on element 
    page.wait_for_selector('//a[text() = "SwitchTo"]').click(button="right")

    
    # Keyboard - A-Z, 0-9, F1-F12, All special character, Arrow right, Arrow Down, PageUp, Enter, Control, Commond 

    #Sift keyboard button click
    page.wait_for_selector('//a[text() = "SwitchTo"]').click(modifiers=["Shift"]) 

    page.wait_for_selector('//a[text() = "SwitchTo"]').press("A")

    page.wait_for_selector('//a[text() = "SwitchTo"]').press("$")

    