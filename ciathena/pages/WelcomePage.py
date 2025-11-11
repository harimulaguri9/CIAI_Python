from datetime import time
from playwright.sync_api import Page
import time
from ciathena.pages.BasePage import BasePage

class WelcomePage(BasePage):
    def __init__(self, page: Page,step_logger=None):
        super().__init__(page,step_logger)
        self.welcome_text=page.locator("#welcome-prefix")
        self.welcome_search_input=page.locator("#welcome-search-input")
        self.search_button=page.locator("#welcome-search-submit-button")
        self.mmx_usecase=page.locator("#app-mmx")
        self.navbar=page.locator("#navbar-deepdive-text-section")

    async def select_usecase(self):
        await self.welcome_search_input.click()
        await self.mmx_usecase.click()
        time.sleep(15)

