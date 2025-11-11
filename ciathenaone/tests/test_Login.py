from datetime import time
import time

import pytest
#from playwright.sync_api import sync_playwright, expect
import asyncio
from playwright.async_api import async_playwright


from ciathena.pages.BasePage import BasePage
from ciathena.pages.InsightsHubPage import InsightsHub
from ciathena.pages.LoginPage import Login
# from ciathena.pages.OngoingThreadsPage import OngoingThreadsPage
# from ciathena.pages.WelcomePage import WelcomePage
# from ciathena.pages.CollabSpacePage import CollabSpacePage


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_login_functionality():
        async with async_playwright() as p:
                browser = await p.chromium.launch(headless=False)
                page = await browser.new_page()
                basepage = BasePage(page)

                await page.goto(
                        "https://ciathena-qa.customerinsights.ai/",
                        wait_until="domcontentloaded",  # Don't wait for full load
                        timeout=60000  # Increase timeout to 60s
                )
                #await page.goto("https://ciathena-qa.customerinsights.ai/")

                login=LoginPage(page)
                #step_logger("Login page success")
                #
                # landing=WelcomePage(page,step_logger)
                # #step_logger("WelcomePage success")

                # ongoingthreads=OngoingThreads(page,step_logger)
                # #step_logger("OngoingThreads page displayed")
                #
                # insightshub=InsightsHub(page,step_logger)
                # #step_logger("InsightsHub page displayed")
                #
                # collabspace = CollabSpacePage(page, step_logger)

                await login.login()
                #collabspace.create_space()

                #await landing.select_usecase()

                # await ongoingthreads.verify_ongoing_threads_UI()
                # await ongoingthreads.ask_question()
                # #time.sleep(40)
                # await ongoingthreads.save_insights()
                # await ongoingthreads.click_unsave_insights_button()
                # await ongoingthreads.share_insights()
                # await ongoingthreads.click_download_insights_button()
                # await ongoingthreads.validate_sql_button()
                # await ongoingthreads.click_info_button()
                # await ongoingthreads.click_like_button()
                # await ongoingthreads.click_dislike_button()
                # await ongoingthreads.verify_suggested_questions()

                #insightshub.verify_insightshub_UI()

                #insightshub.verify_executive_cards()
                #insightshub.verify_chart_details()
                #insightshub.verify_personalized_insights2()
                #insightshub.verify_personalized_insights0()
                #insightshub.verify_personalized_insights_all_sections()

                #collabspace.create_new_space()
                #collabspace.member_sharing()
                #collabspace.rename_spaces()
                #collabspace.delete_spaces()

                #collabspace.create_Dashboard()

                await browser.close()
