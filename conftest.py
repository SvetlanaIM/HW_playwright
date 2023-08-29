import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as Playwright:
        browser = Playwright.chromium.launch(headless=False, slow_mo=100)
        yield browser
        browser.close()