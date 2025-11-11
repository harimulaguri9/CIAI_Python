import time

from playwright.sync_api import sync_playwright

with sync_playwright() as play:
    browser=play.chromium.launch(headless=False)
    page= browser.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html")
    time.sleep(3)
#promptalert

    page.get_by_role("link", name="Alert with OK & Cancel").click()
    time.sleep(3)
    page.locator("#CancelTab").click()
    time.sleep(2)
    page.on("dialog", lambda dialog: dialog.message())
    page.locator("#CancelTab").click()

    time.sleep(3)

    time.sleep(3)
