import re
from datetime import time
import time

import playwright
import pytest
from playwright.sync_api import sync_playwright, expect

from ciathenaone.pages.Login import Login
from ciathenaone.pages.InsightsHub import InsightsHub
from ciathenaone.pages.OngoingThreads import OngoingThreads
from ciathenaone.pages.WelcomePage import WelcomePage


@pytest.mark.smoke
def test_login_functionality(step_logger):
        with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)
                page = browser.new_page()
                page.goto("https://ciathena-qa.customerinsights.ai")
                time.sleep(4)
                expect(page.get_by_text("Sign in with Microsoft")).to_be_visible(timeout=10000)
                time.sleep(5)
                step_logger("navigate to signin page - success")

                login=Login(page,step_logger)
                #step_logger("Login page success")

                landing=WelcomePage(page,step_logger)
                #step_logger("WelcomePage success")

                ongoingthreads=OngoingThreads(page,step_logger)
                #step_logger("OngoingThreads page displayed")

                insightshub=InsightsHub(page,step_logger)
                #step_logger("InsightsHub page displayed")

                login.login()
                landing.select_usecase()
                ongoingthreads.verify_ongoing_threads_UI()
                ongoingthreads.ask_question()
                time.sleep(40)
                ongoingthreads.save_insights()
                time.sleep(3)
                ongoingthreads.click_unsave_insights_button()
                ongoingthreads.share_insights()
                ongoingthreads.click_download_insights_button()
                ongoingthreads.validate_sql_button()
                ongoingthreads.click_info_button()
                ongoingthreads.click_like_button()
                ongoingthreads.click_dislike_button()

                ongoingthreads.verify_suggested_questions()

                #insightshub.verify_insightshub_UI()
                #insightshub.verify_executive_cards()

                browser.close()
