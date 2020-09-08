import unittest
from pages.basepage import BasePage
from values import conf
from webdriver import Driver

class TestPage(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.navigate(conf.URL)

    def test_validate_login_with_valid_username_and_password(self):
        page = BasePage(self.driver)
        page.validate_login_with_valid_username_and_password()

    def test_validate_login_with_invalid_username(self):
        page = BasePage(self.driver)
        page.validate_login_with_invalid_username()

    def test_validate_login_with_invalid_password(self):
        page = BasePage(self.driver)
        page.validate_login_with_invalid_password()

    def test_validate_login_with_invalid_username_and_password(self):
        page = BasePage(self.driver)
        page.validate_login_with_invalid_username_and_password()

    def test_validate_login_with_null_username_field(self):
        page = BasePage(self.driver)
        page.validate_login_with_null_username_field()

    def test_validate_login_with_null_password_field(self):
        page = BasePage(self.driver)
        page.validate_login_with_null_password_field()

    def test_validate_listing_ordering(self):
        page = BasePage(self.driver)
        page.validate_login_with_valid_username_and_password()
        page.validate_listing_ordering()

    def test_validate_pagination(self):
        page = BasePage(self.driver)
        page.validate_login_with_valid_username_and_password()
        page.validate_pagination()

    def test_validade_click_button_swith(self):
        page = BasePage(self.driver)
        page.validate_login_with_valid_username_and_password()
        page.validade_click_button_swith()