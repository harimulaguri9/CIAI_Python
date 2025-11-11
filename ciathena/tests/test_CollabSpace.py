from datetime import time
import time

import pytest
from playwright.sync_api import sync_playwright, expect

from ciathena.pages.BasePage import BasePage
from ciathena.pages.InsightsHubPage import InsightsHubPage
from ciathena.pages.LoginPage import LoginPage
from ciathena.pages.WelcomePage import WelcomePage


@pytest.fixture()
def setup(step_logger):
    # @pytest.mark.smoke
    # def test_login_functionality(step_logger):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        basepage = BasePage(page, step_logger)

        basepage.goto("https://ciathena-qa.customerinsights.ai/")
        loginPage = LoginPage(page, step_logger)
        welcomePage = WelcomePage(page, step_logger)
        insightshubPage = InsightsHubPage(page, step_logger)

        loginPage.login()
        welcomePage.select_usecase()
        time.sleep(5)
        yield insightshubPage  # <-- share with tests
        browser.close()


# @pytest.mark.smoke
# def test_verify_executive_insights(setup):
#     insightshub = setup
#     insightshub.verify_insightshub_UI()
#     insightshub.verify_executive_cards()
#     insightshub.verify_chart_details()
#

@pytest.mark.smoke
def test_verify_personalized_insights(setup):
    insightshub = setup
    # insightshub.verify_personalized_insights2()
    # insightshub.verify_personalized_insights0()
    insightshub.verify_personalized_insights_all_sections()

                #collabspace.create_new_space()
                #collabspace.member_sharing()
                #collabspace.rename_spaces()
                #collabspace.delete_spaces()

                #collabspace.create_Dashboard()