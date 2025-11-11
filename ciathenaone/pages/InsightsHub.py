import re
from datetime import time
from playwright.sync_api import Page, expect
import time
from ciathena.pages.BasePage import BasePage

class InsightsHub(BasePage):
    def __init__(self, page: Page,step_logger=None):
        super().__init__(page,step_logger)
        self.insights_hub_title = page.get_by_text("Insights Hub")
        self.executive_insights_tab = page.locator("#text_executive_insights")
        self.personalized_insights_tab = page.locator("#text_personalized_insights")

        self.executive_insights_card_title1 = page.locator("//h6[contains(@id,'executive-insight-title-')]")
        self.executive_insights_cards_title2 = page.locator("//*[@id='dashboard-header']/p")
        self.executive_insights_cards_details_button = page.locator(
            "//button[contains(@id,'executive-insight-details-btn-')]")
        # self.titles = page.locator('[id^="executive-insight-title-"]')
        self.executive_insights_cards_summary = page.locator("#answer-text-paragraph")
        self.insights_graph_info_button = page.locator("//button[contains(@id,'info-btn-')]")
        # self.insights_tabular_view=page.locator("#toggle-label-0-0")
        self.insights_tabular_toggle_button = page.locator("//div[contains(@id,'toggle-btn-')]")
        self.insights_download_button = page.locator("//button[contains(@id,'download-btn')]")
        self.chart_section_title = page.locator("//div[@data-name='section-header-container']")
        self.detailed_page_back_button = page.locator("#back-button-icon")

        self.personalized_insights_header_content = page.locator("#header-title-content")
        self.personalized_insight_card_content = page.locator(
            "//*[@id='insight-card-data-trends-and-exploration-0']/div[1]/p")
        self.personalized_insight_segmentation_card_content = page.locator(
            "//*[@id='insight-card-segmentation-0']/div[1]/p")
        self.personalized_insight_channels_card_content = page.locator(
            "//*[@id='insight-card-face-to-face-vs-virtual-calls-0']/div[1]/p")
        self.personalized_insight_budget_card_content = page.locator(
            "//*[@id='insight-card-budget-optimization-0']/div[1]/p")

        self.personalized_insight_card_full_content = page.locator(
            "//*[@id='insight-card-data-trends-and-exploration-3']")

        # self.personalized_insight_card_msg_icon = page.locator("#conversation-icon-data-trends-and-exploration-0")
        self.navigate_left_icon = page.locator("#navigate-left-icon")
        self.navigate_right_icon = page.locator("#navigate-right-icon")
        self.personalized_insight_card_title = page.locator("")
        self.tabular_view_toggle = page.locator("#conversation-icon-segmentation-1")
        self.navigate_more_option = page.locator("#more-options-icon-segmentation-0")
        self.Go_to_conversation = page.locator("//*[@id='conversation-btn-data-trends-and-exploration-1']/button")
        #      self.card_more_option=page.locator("//*[@id='more-options-icon-data-trends-and-exploration-0']")

        self.rename_insights_option = self.page.locator('[data-name="rename-action-icon"]')
        self.rename_popup = self.page.locator("#rename-dialog-title-text")
        self.rename_input_field = self.page.locator("#rename-input-field")
        self.rename_confirm_button = self.page.locator("#rename-confirm-button")

        self.collab_space_navbar = page.locator("#sidebar-nav-label-container-collaboration-space")
        self.proceed_button = page.locator("//button[contains(text(), 'Proceed')]")
        self.spaceTitleInput = page.locator("#spaceTitleInput")
        self.spaceDescriptionInput = page.locator("#spaceDescriptionInput")
        self.saveSpaceButton = page.locator("//button[contains(text(), 'Save')]")
        self.MySpace_header = page.locator("//p[normalize-space()='My Spaces']")
        self.rename_space = page.locator("//span[text()='Rename']")
        self.rename_input = page.locator("#rename-input-field")
        self.rename_button = page.locator("#rename-confirm-button")

        self.Delete_space = page.locator("//span[text()='Delete']")
        self.Delete_button = page.locator("//*[@id='delete-confirm-button']")

    def create_space(self):
        title1 = "qa1space"
        title1desc = "qa1spacedesc"
        spacename1 = "testHari_space1"
        time.sleep(5)
        self.collab_space_navbar.click()
        time.sleep(3)
        self.page.evaluate("document.body.style.zoom='80%'")
        time.sleep(3)
        self.proceed_button.click()
        time.sleep(3)
        self.spaceTitleInput.fill(title1)
        self.spaceDescriptionInput.fill(title1desc)
        self.saveSpaceButton.click()
        time.sleep(3)
        self.page.locator("text=Space created successfully").wait_for(state="visible", timeout=10000)
        self.collab_space_navbar.hover()
        self.MySpace_header.wait_for(state="visible", timeout=4000)
        self.page.locator("div").filter(has_text=re.compile(r"^space⋯$")).get_by_role("button").click()

        # self.page.locator().click()
        self.Delete_space.click()
        self.Delete_button.click()
        self.Rename_space.click()
        self.rename_input.press("End")
        self.rename_input.type("_Updated")
        self.rename_button.click()

    def verify_insightshub_UI(self):
        self.insights_hub_nav_label.wait_for(state="visible", timeout=10000)
        time.sleep(5)
        self.insights_hub_nav_label.click()
        self.insights_hub_title.wait_for(state="visible", timeout=5000)
       # check.is_true(self.executive_insights_tab.is_visible(), "Executive Insights tab should be visible")
       # check.is_true(self.personalized_insights_tab.is_visible(), "personalized  Insights tab should be visible")

        #   self.assert_visible(self.executive_insights_tab,"Executive insights")

        assert self.personalized_insights_tab.is_visible()
        self.assert_visible(self.personalized_insights_tab, "Personalized insights")

    def verify_executive_cards(self):
        count = self.executive_insights_card_title1.count()
        print(f"🔍 Found {count} executive insights.")

        for i in range(count):
            self.page.wait_for_timeout(3000)

            title_element = self.executive_insights_card_title1.nth(i)

            # ✅ Capture text BEFORE clicking
            try:
                title_text = title_element.text_content(timeout=5000)
                title_text = title_text.strip() if title_text else "N/A"
            except Exception:
                title_text = "N/A"
            print(f"{i + 1}. {title_text}")
            # optional hover (for tooltip/animation)
            title_element.hover()
            time.sleep(1)

            self.click(self.executive_insights_cards_details_button.nth(i), "Details button")
            time.sleep(4)

            # print(f"{i + 1}. {title_text}")

            self.verify_chart_details()
            self.click(self.detailed_page_back_button, "detailed_page_back_button_")
            time.sleep(3)

    def verify_chart_details(self):
        charts = self.chart_section_title.count()
        for i in range(charts):
            time.sleep(3)
            self.assert_visible(self.insights_graph_info_button.nth(i), f"Info icon for chart {i + 1}")
            self.assert_visible(self.insights_tabular_toggle_button.nth(i), f"Tabular toggle icon for chart {i + 1}")
            self.assert_visible(self.insights_download_button.nth(i), f"Download icon for chart {i + 1}")

            # Click safely using nth(i)
            self.click(self.insights_graph_info_button.nth(i), f"insights_graph_info_button_{i}")
            time.sleep(2)

            self.click(self.insights_tabular_toggle_button.nth(i), f"tabular_toggle_button_{i}")
            time.sleep(2)
            self.click(self.insights_tabular_toggle_button.nth(i), f"tabular_toggle_button_{i}_back")
            time.sleep(2)

            self.click(self.insights_download_button.nth(i), f"download_button_{i}")
            time.sleep(2)

            print(f"✅ Chart {i + 1} verified successfully.\n")

    def verify_personalized_insights_all_sections(self):
        """
        Navigate through Insights sections (Data Trends, Segmentation, etc.),
        perform rename + message icon click on first visible card in each section.
        """

        # --- Step 1: Navigate to Personalized Insights tab ---
        time.sleep(5)
        self.insights_hub_nav_label.click()
        self.personalized_insights_tab.wait_for(state="visible", timeout=5000)
        self.click(self.personalized_insights_tab, "personalized_insights_tab")
        time.sleep(8)

        # --- Step 2: Define all section headers to iterate through ---
        headers = [
            "Data Trends and Exploration",
            "Segmentation",
            "Channel Responsiveness",
            "Budget Optimization"
        ]

        # --- Step 3: Loop through each section header ---
        for index, header_name in enumerate(headers, start=1):
            print(f"\n➡️ Navigating to Section {index}: {header_name}")

            # try:
            # Wait for section header to be visible
            header_locator = self.page.locator(f"//h2[text()='{header_name}']")

            #self.click(header_locator, f'{header_locator}')
            time.sleep(3)
            header_locator.wait_for(state="visible", timeout=10000)
            print(f"✅ Section '{header_name}' loaded.")

            # --- Step 4: Get the first visible insight card under this section ---
            trx_card = self.page.locator(
                f"//div[contains(@id, 'insight-card-{header_name.lower().replace(' ', '-')}')]"
            ).first

            trx_card.wait_for(state="visible", timeout=10000)
            trx_text = trx_card.text_content().strip()
            print(f"📈 Found Card: {trx_text}")

            trx_card.hover()
            time.sleep(2)

            # --- Step 5: Click more → rename ---
            more_icon = self.page.locator(
                f"//*[@id='more-options-icon-{header_name.lower().replace(' ', '-').replace('&', 'and')}-0']"
            )
            more_icon.wait_for(state="visible", timeout=10000)
            more_icon.click()
            time.sleep(1)
            time.sleep(1)
            self.rename_insights_option.click()
            time.sleep(1)
            self.rename_input_field.click()
            self.rename_input_field.press("End")
            self.rename_input_field.type("_Updated")
            self.rename_confirm_button.click()
            print("✅ Successfully renamed insight.")
            time.sleep(2)

            # --- Step 6: Hover again and click message icon ---
            trx_card.hover()
            time.sleep(1)

            msg_icon = self.page.locator(
                f"//*[@id='conversation-btn-{header_name.lower().replace(' ', '-').replace('&', 'and')}-0']"
            )
            msg_icon.wait_for(state='visible', timeout=10000)
            msg_icon.scroll_into_view_if_needed()
            msg_icon.click()
            # validation for OGT
            time.sleep(3)
            # self.click(self.page.go_back(), "personalized_insights_tab")
            self.page.go_back(wait_until="domcontentloaded")
            time.sleep(3)

            # Reopen tab (some apps reload page)
            self.click(self.personalized_insights_tab, "personalized_insights_tab")
            time.sleep(5)

        # except Exception as e:
        #     print(f"⚠️ Error in section '{header_name}': {e}")

        # --- Step 7: Click right arrow to move to next section (except last one) ---
            if index < len(headers):
                for i in range(0,index):
                    self.navigate_right_icon.click()

                time.sleep(4)

    print("\n✅ Completed all Insight sections successfully.")


def verify_personalized_insights1(self):
    # Wait for and open the personalized insights section
    time.sleep(5)
    self.insights_hub_nav_label.click()
    self.personalized_insights_tab.wait_for(state="visible", timeout=5000)
    self.click(self.personalized_insights_tab, "personalized_insights_tab")
    time.sleep(3)

    # Get total visible cards
    count = self.personalized_insight_card_content.count()
    print(f"🔍 Found {count} personalized insights on first view.")

    # Define helper to extract visible card titles
    def get_visible_card_titles():
        # titles = []
        # for i in range(self.personalized_insight_card_content.count()):
        #     try:
        #         title = self.personalized_insight_card_content.nth(i).text_content(timeout=3000)
        #         title = title.strip() if title else "N/A"
        #         titles.append(title)
        #     except Exception:
        #         titles.append("N/A")
        # return titles
        count = self.personalized_insight_card_content.count()
        print(f"🔍 Found {count} personalized insights on first view.")

    # Example: get arrows (assuming you have locators defined)
    right_arrow = self.navigate_right_icon
    left_arrow = self.navigate_left_icon

    # Loop through right clicks and log visible titles
    for i in range(4):  # Adjust for number of slides
        titles = get_visible_card_titles()
        print(f"➡️ After {i} right clicks, visible cards: {titles}")
        right_arrow.click()
        time.sleep(2)

    # Optional: Loop back with left arrow
    for i in range(4):
        titles = get_visible_card_titles()
        print(f"⬅️ After {i} left clicks, visible cards: {titles}")
        left_arrow.click()
        time.sleep(2)

    # Continue your detailed card validation logic
    for i in range(count):
        self.page.wait_for_timeout(3000)
        card_element = self.personalized_insight_card_content.nth(i)
        try:
            card_element_info = card_element.text_content(timeout=5000)
            card_element_info = card_element_info.strip() if card_element_info else "N/A"
        except Exception as e:
            card_element_info = "N/A"
            print(f"⚠️ Error reading card {i + 1}: {e}")

        print(f"{i + 1}. {card_element_info}")
        # card_element.hover()
        # time.sleep(2)
        # self.click(self.personalized_insight_card_msg_icon.nth(i), "msg button clicked")
        # time.sleep(4)
        # self.click(self.detailed_page_back_button, "clicked back_button_")
        # time.sleep(3)


def verify_personalized_insights2(self):
    time.sleep(5)
    self.insights_hub_nav_label.click()
    self.personalized_insights_tab.wait_for(state="visible", timeout=5000)
    self.click(self.personalized_insights_tab, "personalized_insights_tab")
    time.sleep(3)

    # Define helper to extract visible card titles and descriptions
    def get_visible_card_titles_and_info():
        try:
            header_text = self.personalized_insights_header_content.text_content(timeout=3000)
            print(f"\n📊 Header: {header_text.strip()}")
        except Exception:
            print("⚠️ Header not found!")

        card_count = self.personalized_insight_card_content.count()
        cards_data = []
        for i in range(card_count):
            try:
                card_element = self.personalized_insight_card_content.nth(i)
                card_text = card_element.text_content(timeout=3000)
                card_text = card_text.strip().replace("\n", " ") if card_text else "N/A"
                cards_data.append(card_text)
            except Exception:
                cards_data.append("N/A")
        return cards_data

    # Define arrow buttons
    right_arrow = self.navigate_right_icon
    left_arrow = self.navigate_left_icon

    # Log initial set of visible cards
    initial_cards = get_visible_card_titles_and_info()
    print(f"\n➡️ Initial visible cards ({len(initial_cards)}):")
    for card in initial_cards:
        print(f"   • {card}")

    # Loop through slides using right arrow and log new card sets
    for i in range(4):  # Adjust based on how many slides exist
        right_arrow.click()
        time.sleep(2)  # Allow animation
        cards = get_visible_card_titles_and_info()
        print(f"\n➡️ After {i + 1} right click(s), visible cards:")
        for card in cards:
            print(f"   • {card}")

    # (Optional) Loop back with left arrow
    for i in range(4):
        left_arrow.click()
        time.sleep(2)
        cards = get_visible_card_titles_and_info()
        print(f"\n⬅️ After {i + 1} left click(s), visible cards:")
        for card in cards:
            print(f"   • {card}")

    print("\n✅ Completed reading all card data and navigation cycles.\n")


def verify_data_trends_and_cards(self):
    time.sleep(5)
    self.insights_hub_nav_label.click()
    self.personalized_insights_tab.wait_for(state="visible", timeout=5000)
    self.click(self.personalized_insights_tab, "personalized_insights_tab")
    time.sleep(10)
    # --- STEP 1: Read Header ---
    # try:
    header_locator = self.page.locator("text=Data Trends and Exploration")
    header_text = header_locator.text_content(timeout=3000).strip()
    print(f"\n📊 Header: {header_text}")
    time.sleep(2)
    # card_text = self.personalized_insight_card_content.text_content(timeout=5000)
    # time.sleep(2)
    # card_text = card_text.strip() if card_text else "N/A"
    # print(f" card_element_info: {card_text}")

    card_count = self.personalized_insight_card_full_content.count()
    for i in range(card_count):
        card_text1 = self.personalized_insight_card_full_content.text_content(timeout=5000)
        card_item = self.personalized_insight_card_full_content.nth(i)
        card_text1 = card_item.text_content(timeout=3000)
        card_text1 = card_text1.strip().replace("\n", " ") if card_text1 else "N/A"
        print(f"   • Card {i + 1}: {card_text1}")

    print("\n✅ Completed reading header and visible card info...\n")
