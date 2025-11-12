import pytest

# # @pytest.mark.usefixtures("step_logger")
# # @pytest.mark.smoke
# @pytest.mark.asyncio
# async def test_Insights(setup):
#     print("test started")
#     insightshubPage = setup
#     await insightshubPage.verify_personalized_insights_all_sections()

# @pytest.mark.asyncio
# async def test_verify_executive_insights(setup):
#     insightshubPage = setup
#     await insightshubPage.verify_insightshub_UI()
#     await insightshubPage.verify_executive_cards()
#     await insightshubPage.verify_chart_details()

@pytest.mark.usefixtures("step_logger")
@pytest.mark.smoke
@pytest.mark.asyncio
async def test_Insights(setup):
    basepage = setup["basepage"]
    loginPage = setup["loginPage"]
    insightshubPage = setup["insightshubPage"]

    print("✅ Navigation completed!")

    await loginPage.login()
    await insightshubPage.verify_personalized_insights_all_sections()


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_Insights_1(setup):
    basepage = setup["basepage"]
    loginPage = setup["loginPage"]
    insightshubPage = setup["insightshubPage"]

    print("🔹 Starting navigation 111...")
    # await basepage.navigate("https://ciathena-qa.customerinsights.ai/")
    print("✅ Navigation completed! 1111")

    await loginPage.login()
    await insightshubPage.verify_personalized_insights_all_sections()


