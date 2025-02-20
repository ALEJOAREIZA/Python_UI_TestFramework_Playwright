import pytest
from playwright.sync_api import sync_playwright


class BaseTest:
    
    @pytest.fixture(scope="function", autouse=True)
    def before_each_after_each(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome",headless=False)
            self.page = browser.new_page()
            self.page.goto("http://playwright.dev")
            print(self.page.title())
            yield
            browser.close()