
import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ciathena-dev.customerinsights.ai/login")
    page.get_by_role("button", name="Sign in with Microsoft").click()
    page.get_by_role("textbox", name="You'r Email Address").click()
    page.get_by_role("textbox", name="You'r Email Address").fill("hari.mulaguri@customerinsights.ai")
    page.get_by_role("textbox", name="You'r Email Address").press("Enter")
    page.get_by_role("button", name="Next").click()
    page.locator(".pagination-view > div > div:nth-child(3)").click()
    page.get_by_role("textbox", name="Password").fill("Ganesha@123")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("button", name="Text +XX XXXXXXXX73‎").click()
    page.get_by_role("textbox", name="Enter code").click()
    #page.get_by_role("textbox", name="Enter code").fill("796746")
    time.sleep(20)
    page.get_by_role("button", name="Verify").click()
    page.get_by_role("button", name="Yes").click()
    page.goto("https://ciathena-dev.customerinsights.ai/welcome")
    page.get_by_role("button", name="Search Icon").click()
    page.get_by_role("img", name="MMM Icon").click()
    page.get_by_text("Collab").click()
    page.get_by_text("Collab", exact=True).click()
    page.get_by_role("button", name="View View").click()
    page.get_by_role("button", name="Generate dashboard").click()
    page.locator("#infographic-checkbox-0").check()
    page.get_by_text("KPI Cards").click()
    page.locator("#kpi-checkbox-0").check()
    page.get_by_role("button", name="Save and Proceed").click()
    page.get_by_role("textbox", name="Input dashboard name...").click()
    page.get_by_role("textbox", name="Input dashboard name...").fill("dashboardtest1")
    page.get_by_role("textbox", name="Input dashboard name...").press("ControlOrMeta+a")
    page.get_by_role("textbox", name="Input dashboard name...").press("ControlOrMeta+c")
    page.get_by_role("textbox", name="Input here....").click(modifiers=["ControlOrMeta"])
    page.get_by_role("textbox", name="Input here....").fill("dashboardtest1desc")
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="Edit").click()
    page.locator("#collaboration-space-dashboard-title-edit-input").click()
    page.locator("#collaboration-space-dashboard-title-edit-input").click()
    page.locator("#collaboration-space-dashboard-title-edit-input").click()
    page.locator("#collaboration-space-dashboard-title-edit-input").press("ArrowRight")
    page.locator("#collaboration-space-dashboard-title-edit-input").press("ArrowRight")
    page.locator("#collaboration-space-dashboard-title-edit-input").fill("dashboardtest123")
    page.get_by_role("button", name="Save").click()
    page.goto("https://ciathena-dev.customerinsights.ai/deepdive?section=collaboration-space&appId=mmx&appName=MMM&tab=generate-dashboard&dashboard=7a130a5e-2be2-4563-85a8-f1f4150cecb2")
    page.get_by_role("button", name="Share").click()
    page.locator("#spaceInfoContainer-0").click()
    page.locator("#spaceInfoContainer-0").get_by_text("qa1space").click()
    page.get_by_role("button", name="Cancel").click()
    page.get_by_role("button", name="Share").click()
    page.locator("#spaceMembersInfo-0").get_by_text("members").click()
    page.locator("#spaceInfoContainer-0").get_by_text("qa1space").click()
    page.locator("#spaceInfoContainer-0").get_by_text("qa1space").click()
    page.get_by_text("Add to spacesAdd to").click()
    page.get_by_text("SaveCancel").click()
    page.get_by_role("button", name="Refresh dashboard").click()
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Download as PDF").click()
    download = download_info.value
    with page.expect_download() as download1_info:
        page.locator("#collaboration-space-dashboard-actions-container").click()
    download1 = download1_info.value

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
