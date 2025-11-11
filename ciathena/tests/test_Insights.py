import pytest

@pytest.mark.usefixtures("step_logger")
@pytest.mark.smoke
@pytest.mark.asyncio
async def test_Insights(setup):
    insightshubPage = setup
    await insightshubPage.verify_personalized_insights_all_sections()

@pytest.mark.smoke
@pytest.mark.asyncio
async def test_verify_executive_insights(setup):
    insightshubPage = setup
    await insightshubPage.verify_insightshub_UI()
    await insightshubPage.verify_executive_cards()
    await insightshubPage.verify_chart_details()
