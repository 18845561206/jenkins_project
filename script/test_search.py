# from base.base_driver import init_driver
# from page.page import Page
# import pytest
# import time
# import allure
# class TestSearch:
#     def setup(self):
#         self.driver = init_driver()
#         self.page = Page(self.driver)
#     @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
#     @pytest.mark.parametrize("args", ["hello1", "xiaoming"])
#     def test_search(self, args):
#         self.page.setting.click_search()
#         self.page.search.input_key_word(args)
#         time.sleep(3)
#         self.page.search.click_back()
#
#     @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
#     def test_login(self):
#         print("1")
#         assert 0
#     def teardown(self):
#         time.sleep(3)
#         self.driver.quit()
