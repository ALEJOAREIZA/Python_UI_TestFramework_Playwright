from base_test import BaseTest
from playwright.sync_api import expect

class Test_Example(BaseTest):
    
    def test_main_navigation(self):
        expect(self.page).to_have_url("https://playwright.dev/")