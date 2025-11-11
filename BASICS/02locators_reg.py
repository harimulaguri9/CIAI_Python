from playwright.sync_api import sync_playwright

with sync_playwright() as play:
    browser=play.chromium.launch(headless=False)
    page= browser.new_page()
    page.goto("https://demo.automationtesting.in/Index.html")

#id | . class | xpth tagname[@att='value'] |

    page.locator("#btn2").click()
    page.get_by_placeholder("First Name").fill("Hari")
    page.locator("")
    page.get_by_placeholder("Last Name").fill("kumar")
    page.locator("//textarea[@ng-model='Adress']").fill("bangalore")
    page.locator("//input[@type='email']").fill("haritest@gmail.com")
    page.locator("")
    page.locator("//input[@type='tel']").fill("1234567890")
    page.locator("//input[@name='radiooptions' and @value='Male']").click()
    page.locator("//input[@id='checkbox1' and @value='Cricket']").click()

    page.wait_for_selector("#msdd").click()
    page.wait_for_selector("//select[contains(@id,'Skills')]").click()

#drop_downs
    page.select_option('//*[@id="Skills"]',label='AutoCAD')
    page.wait_for_timeout(2000)



#radio_button
    radiobutton=page.query_selector('//input[@value="Male"]')
    radiobutton.check()
    if radiobutton.is_checked():
        print("radiobutton- checked")
    page.wait_for_timeout(3000)

#checkbox_button
    checkcbox=page.query_selector('//input[@value="Cricket"]')
    checkcbox.check()
    if checkcbox.is_checked():
        print("checkbox is checked")
    page.wait_for_timeout(3000)


#promptalert
