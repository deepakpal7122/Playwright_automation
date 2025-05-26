from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    try:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = browser.new_page()
        page.goto("https://demo.automationtesting.in/Selectable.html")

        # Store multiple elemnet using list
        elements = page.query_selector_all('b')
        print(len(elements))
        for i in elements:
            print(i.text_content())

        page.wait_for_timeout(2000)

        # print all link in terminal
        links = page.query_selector_all('a')
        print(len(links))
        for i in links:
            print(i.get_attribute('href'))

        page.wait_for_timeout(2000) 

    except Exception as e:
        print(str(e))

    finally:
        print("Execute")