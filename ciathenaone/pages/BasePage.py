from playwright.async_api import Page, expect
from ciathena.tests.conftest import step_logger



class BasePage:
    def __init__(self, page: Page, step_logger=None):
        self.page = page
        self.step_logger = step_logger  # can be None if not passed

    async def launch(self):
        await page.goto("https://ciathena-qa.customerinsights.ai/")
        await expect(page.get_by_text("Sign in with Microsoft")).to_be_visible(timeout=20000)
        step_logger("navigate to signin page - success")

    async def navigate(self, url: str):
        await self.page.goto(url)

    async def click(self, locator, description: str = ""):
        """
        Custom click method with logging and auto wait.
        :param locator: Playwright locator object
        :param description: Description for log (e.g., 'Login button')
        """
        try:
            if self.step_logger:
                self.step_logger(f"Clicking on {description or locator}")

            # Wait for element to be visible & enabled
            await locator.wait_for(state="visible")

            # Perform click
            await locator.click()

            if self.step_logger:
                self.step_logger(f"Clicked successfully on {description}")

        except Exception as e:
            if step_logger:
                await step_logger(f"❌ Failed to click on {description}: {e}")
            raise

    async def assert_visible(self, locator, description: str = ""):
        """Common assertion to check element visibility"""
        try:
            #self.step_logger(f"Verifying visibility of {description}")
            expect(locator).to_be_visible(timeout=5000)
            await step_logger(f"✅ {description} is visible")
        except Exception as e:
            await self.step_logger(f"❌ {description} is NOT visible: {e}")
            raise