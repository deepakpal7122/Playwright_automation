from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()    # context can store multiple pages value that's why we using this line code 
    page.goto("https://demo.automationtesting.in/Windows.html")


    page.wait_for_selector('//button[text() = "    click   " ]').click()
    page.wait_for_timeout(3000)
    
    # how to find total pages
    total_pages = context.pages
    print(len(total_pages))

    # printing pages url
    for i in total_pages:
        print(i)         

    print(page.title())

    # switch to new page
    new_page = total_pages[1]
    new_page.bring_to_front()

    page.wait_for_timeout(3000)
    print(new_page.title())
    new_page.close()

    page.bring_to_front()
    page.wait_for_timeout(3000)
    browser.close()
