from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    page.goto("https://vinothqaacademy.com/webtable/")

    table = page.wait_for_selector("//table[@id='myTable']/tbody")

    tr = table.query_selector_all('tr')
    print(len(tr))
    td = table.query_selector_all('td')
    print(len(td))

    for row in tr:
        columns = row.query_selector_all('td')
        for column in columns:
            print(column.text_content())