import pytest
from pytest_html import extras

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach step logs to pytest HTML report"""
    outcome = yield
    rep = outcome.get_result()

    if hasattr(item, "step_logs") and rep.when == "call":
        html_steps = "<br>".join(item.step_logs)
        extra = getattr(rep, "extra", [])
        extra.append(
            extras.html(f"<div><strong>Execution Steps:</strong><br>{html_steps}</div>")
        )
        rep.extra = extra


@pytest.fixture
def step_logger(request):
    """Fixture to record step-by-step logs"""
    request.node.step_logs = []

    def log_step(message: str):
        print(f"[STEP] {message}")
        request.node.step_logs.append(f"➡️ {message}")

    return log_step