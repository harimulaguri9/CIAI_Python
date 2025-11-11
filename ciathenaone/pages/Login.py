from datetime import time
from playwright.sync_api import Page
import time
from ciathena.pages.BasePage import BasePage
from ciathena.tests.conftest import step_logger


class Login(BasePage):
    def __init__(self, page: Page,step_logger=None):
        super().__init__(page,step_logger)
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

    def login(self):
        self.click(self.SSO_signin_button,"SSO Signin Button")
        self.email_input.fill("hari.mulaguri@customerinsights.ai")
        self.next_button.click()

        self.password_input.wait_for(state="visible", timeout=3000)
        self.password_input.fill("Ganesha@123")

        self.signin_button.click()
        self.phone_number_button.wait_for(state="visible", timeout=3000)
        self.phone_number_button.click()
        time.sleep(20)
        self.verify_button.click()
        self.yes_button.click()
        self.welcome_text.wait_for(state="visible", timeout=20000)
        self.assert_visible(self.welcome_text,"Welcome on Homepage")
