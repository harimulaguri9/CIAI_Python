
from datetime import time

from playwright.sync_api import Page, expect
import time
from ciathena.pages.BasePage import BasePage

class OngoingThreads(BasePage):
    def __init__(self, page: Page,step_logger=None):
        super().__init__(page,step_logger)
        self.ongoing_threads_title=page.get_by_text("Ongoing Threads")
        self.mmx_title=page.get_by_text("Market Mix Modeling")
        self.home_icon=page.locator("#navbar-home-button")
        self.settings_icon=page.locator("#navbar-settings-button")
        self.app_overview_icon=page.locator("#navbar-app-overview-button")
        self.main_input=page.locator("#main-input")
        self.mic_icon=page.locator("#question-response-mic-button")
        self.show_thinking_button=page.locator("#show-thinking-button")
        self.send_button1 = page.locator("#send-btn")
        self.send_button2=page.locator("#question-response-send-button")
        self.data_category_section=page.locator("#categories-wrapper")
        self.main_input=page.locator("#main-input")
        self.answer_response=page.locator("#answer-text")
        self.share_visualization_button=page.locator("#share-visualization-button")
        self.save_insights_button=page.locator("#save-visualization-button")

#        self.tag1_insight=page.locator("div").filter(has_text=re.compile(r"^Payers$"))
        self.next_button=page.locator("#nextButton")
        self.save_button=page.get_by_role("button", name="Save")
        #self.Unsave_button=page.get_by_role("button", name="Unsave")
        self.submit_button=page.get_by_role("button", name="Submit")
        self.insight_saved_msg=page.get_by_text("Insight saved successfully")
        self.insight_Unsaved_msg=page.get_by_text("Bookmark removed successfully")
        self.download_button=page.locator("#download-visualization-button")
        self.download_visual_button = page.locator("#download-visuals-option")

        self.sql_button=page.locator("#sql-toggle-button")
        self.info_button=page.locator("#info-button")

        self.like_button=page.locator("#like-button")
        self.like_msg = page.locator("#like-icon")
        self.dislike_button = page.locator("#dislike-button")
        self.unlike_feedback_dialog=page.locator("#feedback-dialog-textarea")
        self.feedback_submit_button=page.locator("#feedback-dialog-submit-button")
        self.unlike_msg = page.locator("#like-icon")
        self.tag_containers = page.locator("[id^='tagItem-']")
        self.cancel_button=page.locator("#cancelButton")
        self.space_containers = page.locator("[id^='spaceInfoContainer-']")
        self.create_space_button=page.locator("button:has(span.MuiTouchRipple-root)")
        self.space_title_input=page.locator("#spaceTitleInput")
        self.space_desc_input = page.locator("#spaceDescriptionInput")
        self.space_save_input = page.locator("#saveSpaceButton")
        self.space_cancel_input = page.locator("#cancelSpaceCreationButton")
        self.space_create_space_popup = page.locator("#spaceTitleInput")
        self.save_ToSpace_Button=page.locator("#saveToSpaceButton")

        self.suggested_questions_title=page.locator("#suggested-questions-title")
        #self.suggested_questions_list=page.locator("//*[@id='suggested-questions-list']")
        self.suggested_questions_icon=page.locator("#suggested-question-arrow-icon-0")
        self.suggested_questions_list=page.locator("#suggested-question-item-0")

    def verify_ongoing_threads_UI(self):
        self.ongoing_threads_title.wait_for(state="visible", timeout=20000)
        assert self.mmx_title.is_visible()
        self.assert_visible(self.mmx_title,"MMX title ")

        assert self.home_icon.is_visible()
        self.assert_visible(self.home_icon,"home_icon ")

        assert self.settings_icon.is_visible()
        self.assert_visible(self.settings_icon,"settings_icon  ")

        assert self.app_overview_icon.is_visible()
        self.assert_visible(self.app_overview_icon,"app_overview_icon ")


    def ask_question(self):
        self.main_input.fill("What is the MoM percentage change in TOTAL_DIGITAL_PROMOTIONS at the specialty group level?")
        self.send_button1.click()
        time.sleep(10)
        self.assert_visible(self.show_thinking_button,"show_thinking_button ")

        if self.answer_response.is_visible():
            return self.answer_response.text_content().strip()
        return None

    def tags_select(self):
        count = self.tag_containers.count()
        target_tag_name = "testtag"
        for i in range(count):
            tag_element = self.tag_containers.nth(i)
            tag_name_text = tag_element.text_content().strip()
            print(f"🔹 Found tag: {tag_name_text}")

            # Check if tag name matches your target
            if target_tag_name.lower() in tag_name_text.lower():
                print(f"✅ Matching tag found: {tag_name_text}")
                tag_element.click()
                print(f"✅ Matching tag: '{tag_name_text}' clicked")
                break
        else:
            print(f"⚠️Tag: '{target_tag_name}' not found!")

    def space_select(self):
        count = self.space_containers.count()
        target_space_name = "Hari_prod_space5"
        for i in range(count):
            space_element = self.space_containers.nth(i)
            name_text = space_element.text_content().strip()
            print(f"🔹Found space: {name_text}")

            # Check if space name matches your target
            if target_space_name.lower() in name_text.lower():
                print(f"✅ Matching space found: {name_text}")
                space_element.click()
                print(f"✅ Matching space : '{name_text}' clicked")

                break
        else:
            print(f"⚠️ Space: '{target_space_name}' not found!")

    def share_insights(self):
        self.share_visualization_button.click()
        time.sleep(3)
        #self.tags_select()
        #time.sleep(3)
        #self.next_button.click()
        #time.sleep(3)
        self.space_select()
        self.save_ToSpace_Button.click()

    def save_insights(self):
        self.save_insights_button.click()
        time.sleep(3)
        self.tags_select()
        time.sleep(3)
        #self.save_button.click()
        time.sleep(2)
        self.submit_button.click()
        time.sleep(3)
        assert self.insight_saved_msg.is_visible()
        self.assert_visible(self.insight_saved_msg, "Insight saved successfully")



    def click_unsave_insights_button(self):
        self.save_insights_button.click()
        time.sleep(2)
        assert self.insight_Unsaved_msg.is_visible()
        self.assert_visible(self.insight_Unsaved_msg, "Bookmark removed successfully")
        time.sleep(2)

    def click_download_insights_button(self):
        self.click(self.download_button, "download_button")
        time.sleep(3)
        self.click(self.download_visual_button, "download_visual_button")
        time.sleep(3)

    def click_info_button(self):
        self.click(self.info_button, "info_button")
        time.sleep(3)

    def validate_sql_button(self):
        self.click(self.sql_button, "sql_button")
        time.sleep(3)
        expect(self.sql_button).to_have_attribute("aria-label", "Hide SQL")
        time.sleep(2)
        self.click(self.sql_button, "sql_button")
        time.sleep(2)
        expect(self.sql_button).to_have_attribute("aria-label", "Show SQL")




    def click_hide_sql_button(self):
        self.click(self.sql_button, "sql_button")

        time.sleep(3)
    def click_like_button(self):
        self.click(self.like_button, "like_button")
        time.sleep(2)
        expect(self.like_button).to_have_attribute("aria-label", "Undo like")
        assert self.like_msg.is_visible()
        time.sleep(2)


    def click_dislike_button(self):
        self.click(self.dislike_button, "unlike_button")
        time.sleep(3)
        self.assert_visible(self.unlike_feedback_dialog, "unlike feedback popup")
        self.unlike_feedback_dialog.fill("test unlike feedback")
        time.sleep(2)
        self.click(self.feedback_submit_button, "feedback_submit_button")
        time.sleep(5)

    def verify_suggested_questions(self):
        assert self.suggested_questions_title.is_visible()
        time.sleep(2)
        self.click(self.suggested_questions_list, "suggested question selected")
        self.click(self.send_button2, "clicked on suggested question send_button")
        time.sleep(40)


