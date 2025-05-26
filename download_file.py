from playwright.sync_api import sync_playwright

def download_handle(download):
    location_file = './download_filepath/downloadfilezipfile.zip'
    download.save_as(location_file)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/FileDownload.html")

    # call the download_handle function
    page.on('download', download_handle)
    page.wait_for_selector("//a[@type='button']").click()
    page.wait_for_timeout(8000)
