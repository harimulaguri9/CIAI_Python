import re
from playwright.sync_api import Page, expect, sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://www.facebook.com")
    page.wait_for_timeout(3000)

    print("facebook page loaded success")
    print(page.title())
    browser.close()