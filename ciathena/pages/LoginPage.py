from datetime import time
import time
from ciathena.pages.BasePage import BasePage
#from ciathena.tests.conftest import step_logger
from playwright.async_api import Page


class LoginPage(BasePage):
    def __init__(self, page: Page,step_logger=None):
        super().__init__(page)
        self.SSO_signin_button=page.get_by_text("Sign in with Microsoft")
        self.email_input = page.get_by_role("textbox", name="You'r Email Address")
        self.next_button = page.get_by_role("button", name="Next")
        self.password_input =  page.locator("#i0118")
        self.signin_button =page.locator("#idSIButton9")
       # self.signin_button =page.get_by_role("button", name="Sign in")
        self.phone_number_button=page.get_by_role("button", name="Text +XX XXXXXXXX73")
        self.verify_button=page.get_by_role("button", name="Verify")
        self.yes_button=page.get_by_role("button", name="Yes")
        self.welcome_text=page.locator("#welcome-prefix")

    async def login(self):
        await self.SSO_signin_button.click()
        await self.email_input.fill("hari.mulaguri@customerinsights.ai")
        await self.next_button.click()
        await self.password_input.wait_for(state="visible")
        await self.password_input.fill("Ganesha@123")

        await self.signin_button.click()
        await self.phone_number_button.wait_for(state="visible")
        await self.phone_number_button.click()
        time.sleep(17)
        await self.verify_button.click()
        time.sleep(3)
        await self.yes_button.click()
        time.sleep(5)
        await self.welcome_text.wait_for(state="visible")
        time.sleep(5)
        #await self.assert_visible(self.welcome_text,"Welcome on Homepage")
