from datetime import time
import time

import pytest
from playwright.async_api import async_playwright, expect
from ciathena.pages.BasePage import BasePage
from ciathena.pages.LoginPage import LoginPage
from ciathena.pages.OngoingThreadsPage import OngoingThreadsPage
from ciathena.pages.WelcomePage import WelcomePage

@pytest.mark.usefixtures("step_logger")
@pytest.mark.smoke
@pytest.mark.asyncio
async def test_OngoingThreads(step_logger):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        basepage = BasePage(page, step_logger)

        await basepage.navigate("https://ciathena-qa.customerinsights.ai/")
        loginPage = LoginPage(page, step_logger)
        # step_logger("Login page success")

        welcomePage = WelcomePage(page, step_logger)
        # #step_logger("WelcomePage success")

        ongoingthreads=OngoingThreadsPage(page,step_logger)
        # #step_logger("OngoingThreads page displayed")
        #
        # insightshub=InsightsHub(page,step_logger)
        # #step_logger("InsightsHub page displayed")
        #
        # collabspace = CollabSpacePage(page, step_logger)

        await loginPage.login()
        await welcomePage.select_usecase()
        await ongoingthreads.verify_ongoing_threads_UI()
        await ongoingthreads.ask_question()
        time.sleep(30)
        await ongoingthreads.save_insights()
        await ongoingthreads.click_unsave_insights_button()
        #await ongoingthreads.share_insights()
        await ongoingthreads.click_download_insights_button()
        await ongoingthreads.validate_sql_button()
        await ongoingthreads.click_info_button()
        await ongoingthreads.click_like_button()
        await ongoingthreads.click_dislike_button()
        await ongoingthreads.verify_suggested_questions()
        browser.close()
