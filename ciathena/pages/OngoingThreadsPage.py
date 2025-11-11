import asyncio
import time

from playwright.async_api import Page, expect
from ciathena.pages.BasePage import BasePage


class OngoingThreadsPage(BasePage):
    def __init__(self, page: Page, step_logger=None):
        super().__init__(page, step_logger)
        self.ongoing_threads_title = page.get_by_text("Ongoing Threads")
        self.mmx_title = page.get_by_text("Market Mix Modeling")
        self.home_icon = page.locator("#navbar-home-button")
        self.settings_icon = page.locator("#navbar-settings-button")
        self.app_overview_icon = page.locator("#navbar-app-overview-button")
        self.main_input = page.locator("#main-input")
        self.mic_icon = page.locator("#question-response-mic-button")
        self.show_thinking_button = page.locator("#show-thinking-button")
        self.send_button1 = page.locator("#send-btn")
        self.send_button2 = page.locator("#question-response-send-button")
        self.data_category_section = page.locator("#categories-wrapper")
        self.answer_response = page.locator("#answer-text")
        self.share_visualization_button = page.locator("#share-visualization-button")
        self.save_insights_button = page.locator("#save-visualization-button")
        self.next_button = page.locator("#nextButton")
        self.save_button = page.get_by_role("button", name="Save")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.insight_saved_msg = page.get_by_text("Insight saved successfully")
        self.insight_unsaved_msg = page.get_by_text("Bookmark removed successfully")
        self.insight_shared_msg = page.get_by_text("Insight shared successfully")
        self.download_button = page.locator("#download-visualization-button")
        self.download_visual_button = page.locator("#download-visuals-option")
        self.sql_button = page.locator("#sql-toggle-button")
        self.info_button = page.locator("#info-button")
        self.like_button = page.locator("#like-button")
        self.like_msg = page.locator("#like-icon")
        self.dislike_button = page.locator("#dislike-button")
        self.unlike_feedback_dialog = page.locator("#feedback-dialog-textarea")
        self.feedback_submit_button = page.locator("#feedback-dialog-submit-button")
        self.unlike_msg = page.locator("#like-icon")
        self.tag_containers = page.locator("[id^='tagItem-']")
        self.cancel_button = page.locator("#cancelButton")
        self.space_containers = page.locator("[id^='spaceInfoContainer-']")
        self.create_space_button = page.locator("button:has(span.MuiTouchRipple-root)")
        self.space_title_input = page.locator("#spaceTitleInput")
        self.space_desc_input = page.locator("#spaceDescriptionInput")
        self.tag_items = page.locator("#tagItem-")

        self.space_save_input = page.locator("#saveSpaceButton")
        self.space_cancel_input = page.locator("#cancelSpaceCreationButton")
        self.space_create_space_popup = page.locator("#spaceTitleInput")
        self.save_to_space_button = page.locator("#saveToSpaceButton")
        self.suggested_questions_title = page.locator("#suggested-questions-title")
        self.suggested_questions_icon = page.locator("#suggested-question-arrow-icon-0")
        self.suggested_questions_list = page.locator("#suggested-question-item-0")

    # --------------------------------------------------------------------------
    # Verification of page UI
    # --------------------------------------------------------------------------
    async def verify_ongoing_threads_UI(self):
        await self.ongoing_threads_title.wait_for(state="visible", timeout=20000)
        await self.assert_visible(self.mmx_title, "MMX title")
        await self.assert_visible(self.home_icon, "home_icon")
        await self.assert_visible(self.settings_icon, "settings_icon")
        await self.assert_visible(self.app_overview_icon, "app_overview_icon")

    # --------------------------------------------------------------------------
    # Ask Question
    # --------------------------------------------------------------------------
    async def ask_question(self):
        await self.main_input.fill(
            "What is the MoM percentage change in TOTAL_DIGITAL_PROMOTIONS at the specialty group level?"
        )
        await self.send_button1.click()
        #await asyncio.sleep(3)
        await self.assert_visible(self.show_thinking_button, "show_thinking_button")
        time.sleep(20)
        if await self.answer_response.is_visible():
            text = await self.answer_response.text_content()
            return text.strip() if text else None
        return None

    # --------------------------------------------------------------------------
    # Tag selection
    # --------------------------------------------------------------------------
    # async def tags_select(self):
    #     count = await self.tag_containers.count()
    #     target_tag_name = "testhari"
    #
    #     for i in range(count):
    #         tag_element = self.tag_containers.nth(i)
    #         tag_name_text = (await tag_element.text_content() or "").strip()
    #         print(f"🔹 Found tag: {tag_name_text}")
    #
    #         if target_tag_name.lower() in tag_name_text.lower():
    #             print(f"✅ Matching tag found: {tag_name_text}")
    #             await tag_element.click()
    #             print(f"✅ Matching tag: '{tag_name_text}' clicked")
    #             break
    #     else:
    #         print(f"⚠️ Tag: '{target_tag_name}' not found!")
    async def tag_select(self):
        count = await self.tag_items.count()
        target_space_tag_name = "hari_tag"

        for i in range(count):
            tag_space_element = self.tag_items.nth(i)
            print(tag_space_element)
            tag_name_text = (await tag_space_element.text_content() or "").strip()
            print(f"🔹 Found space: {tag_name_text}")

            if target_space_tag_name.lower() in tag_name_text.lower():
                print(f"✅ Matching space found: {tag_name_text}")
                await tag_space_element.click()
                print(f"✅ Matching space: '{tag_name_text}' clicked")
                break
        else:
            print(f"⚠️ Space: '{target_space_tag_name}' not found!")

    # --------------------------------------------------------------------------
    # Space selection
    # --------------------------------------------------------------------------
    async def space_select(self):
        count = await self.space_containers.count()
        target_space_name = "qa1space"

        for i in range(count):
            space_element = self.space_containers.nth(i)
            space_name_text = (await space_element.text_content() or "").strip()
            print(f"🔹 Found space: {space_name_text}")

            if target_space_name.lower() in space_name_text.lower():
                print(f"✅ Matching space found: {space_name_text}")
                await space_element.click()
                print(f"✅ Matching space: '{space_name_text}' clicked")
                break
        else:
            print(f"⚠️ Space: '{target_space_name}' not found!")

    # --------------------------------------------------------------------------
    # Share Insights
    # --------------------------------------------------------------------------
    async def share_insights(self):
        await self.share_visualization_button.click()
       # await asyncio.sleep(3)
        await self.tag_select()
        await asyncio.sleep(3)
        await  self.next_button.click()
        await self.space_select()
        await asyncio.sleep(3)
        await self.save_to_space_button.click()
       # await asyncio.sleep(2)
        await expect(self.insight_shared_msg).to_be_visible(timeout=5000)
        await self.assert_visible(self.insight_shared_msg, "Insight shared successfully")
    # --------------------------------------------------------------------------
    # Save Insights
    # --------------------------------------------------------------------------
    async def save_insights(self):
        await self.save_insights_button.click()
      #  await asyncio.sleep(3)
        await self.tag_select()
      #  await asyncio.sleep(3)
        await self.submit_button.click()
     #   await asyncio.sleep(3)
        await expect(self.insight_saved_msg).to_be_visible(timeout=5000)
        await self.assert_visible(self.insight_saved_msg, "Insight saved successfully")

    # --------------------------------------------------------------------------
    # Unsave Insights
    # --------------------------------------------------------------------------
    async def click_unsave_insights_button(self):
        await self.save_insights_button.click()
     #   await asyncio.sleep(2)
        await expect(self.insight_unsaved_msg).to_be_visible(timeout=5000)
        await self.assert_visible(self.insight_unsaved_msg, "Bookmark removed successfully")
       # await asyncio.sleep(2)

    # --------------------------------------------------------------------------
    # Download Insights
    # --------------------------------------------------------------------------
    async def click_download_insights_button(self):
        await self.click(self.download_button, "download_button")
       # await asyncio.sleep(3)
        await self.click(self.download_visual_button, "download_visual_button")
       # await asyncio.sleep(3)

    # --------------------------------------------------------------------------
    # Info Button
    # --------------------------------------------------------------------------
    async def click_info_button(self):
        await self.click(self.info_button, "info_button")
       # await asyncio.sleep(3)

    # --------------------------------------------------------------------------
    # SQL Button Validation
    # --------------------------------------------------------------------------
    async def validate_sql_button(self):
        await self.click(self.sql_button, "sql_button")
      #  await asyncio.sleep(3)
        await expect(self.sql_button).to_have_attribute("aria-label", "Hide SQL")
     #   await asyncio.sleep(2)
        await self.click(self.sql_button, "sql_button")
     #   await asyncio.sleep(2)
        await expect(self.sql_button).to_have_attribute("aria-label", "Show SQL")

    # --------------------------------------------------------------------------
    # Like & Dislike Buttons
    # --------------------------------------------------------------------------
    async def click_like_button(self):
        await self.click(self.like_button, "like_button")
      #  await asyncio.sleep(2)
        await expect(self.like_button).to_have_attribute("aria-label", "Undo like")
        await expect(self.like_msg).to_be_visible(timeout=5000)
      #  await asyncio.sleep(2)

    async def click_dislike_button(self):
        await self.click(self.dislike_button, "unlike_button")
      #  await asyncio.sleep(3)
        await self.assert_visible(self.unlike_feedback_dialog, "unlike feedback popup")
        await self.unlike_feedback_dialog.fill("test unlike feedback")
     #   await asyncio.sleep(2)
        await self.click(self.feedback_submit_button, "feedback_submit_button")
     #   await asyncio.sleep(5)

    # --------------------------------------------------------------------------
    # Suggested Questions
    # --------------------------------------------------------------------------
    async def verify_suggested_questions(self):
        await expect(self.suggested_questions_title).to_be_visible(timeout=10000)
       # await asyncio.sleep(2)
        await self.click(self.suggested_questions_list, "suggested question selected")
        await self.click(self.send_button2, "clicked on suggested question send_button")
      #  await asyncio.sleep(40)
