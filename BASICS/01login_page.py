from playwright.sync_api import sync_playwright

with sync_playwright() as play:
    browser=play.chromium.launch(headless=False)
    page= browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(5000)

    username=page.wait_for_selector('input[name="username"]')  #xpath
    username.type("Admin")
    page.wait_for_timeout(3000)

    password=page.wait_for_selector('input[name="password"]')
    password.type("admin123")
    page.wait_for_timeout(3000)

    login=page.wait_for_selector('button[type="submit"]')
    login.click()

    page.wait_for_timeout(3000)
