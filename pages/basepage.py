from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def username(self, tx_user):
        WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_element_located((
                By.ID, "normal_login_username"))).send_keys(tx_user)

    def password(self, tx_password):
        WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_element_located((
                By.ID, "normal_login_password"))).send_keys(tx_password)

    def login(self):
        WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_element_located((
                By.XPATH, "//button[@class='ant-btn login-form-button ant-btn-primary']"))).click()

    def page(self, tx_name_page):
        WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                "//nav[@class='Navigation_Navigation__1Ylka']//span[contains(.,'" + tx_name_page + "')]"))).click()


    def radioButton(self, tx_name_button):
        WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                "//input[@class='ant-radio-button-input']/../..//span[contains(.,'"+ tx_name_button +"')]"))).click()


    def validate_login_with_valid_username_and_password(self):
        self.username("testuser")
        self.password("pl123")
        self.login()
        msg = self.driver.instance.find_element_by_xpath("//div[@class='welcome']")

        assert "Hi, Test User" in msg.text


    def validate_login_with_invalid_username(self):
        self.username("user")
        self.password("pl123")
        self.login()
        msg = self.driver.instance.find_element_by_xpath("//p[@class='error-message']")

        assert "There was a problem logging in: Login/Password is incorrect" in msg.text


    def validate_login_with_invalid_password(self):
        self.username("user")
        self.password("pl1234")
        self.login()
        msg = self.driver.instance.find_element_by_xpath("//p[@class='error-message']")

        assert "There was a problem logging in: Login/Password is incorrect" in msg.text


    def validate_login_with_invalid_username_and_password(self):
        self.username("user")
        self.password("123456")
        self.login()
        msg = self.driver.instance.find_element_by_xpath("//p[@class='error-message']")

        assert "There was a problem logging in: Login/Password is incorrect" in msg.text


    def validate_login_with_null_username_field(self):
        self.password("pl123")
        self.login()
        msg = self.driver.instance.find_element_by_xpath("//div[@class='ant-form-explain']")

        assert "Please input your username." in msg.text


    def validate_login_with_null_password_field(self):
        self.username("testuser")
        self.login()
        msg = self.driver.instance.find_element_by_xpath("//div[@class='ant-form-explain']")

        assert "Please input your Password." in msg.text


    def validate_listing_ordering(self):
        WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_element_located((
                By.XPATH, "//nav[@class='Navigation_Navigation__1Ylka']//span[contains(.,'Page 1')]"))).click()
        WebDriverWait(self.driver.instance, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, "//th[@class='ant-table-column-has-actions ant-table-column-has-sorters']"))).click()

        name = self.driver.instance.find_element_by_xpath("//tr[@class='ant-table-row ant-table-row-level-0'][1]/td[1]")
        borrow = self.driver.instance.find_element_by_xpath("//tr[@class='ant-table-row ant-table-row-level-0'][1]/td[2]")
        repayment = self.driver.instance.find_element_by_xpath("//tr[@class='ant-table-row ant-table-row-level-0'][1]/td[3]")

        assert "Willard Medina" in name.text
        assert "728" in borrow.text
        assert "451" in repayment.text

        WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_element_located((
                By.XPATH, "//th[@class='ant-table-column-has-actions ant-table-column-has-sorters ant-table-column-sort']"))).click()

        name = self.driver.instance.find_element_by_xpath("//tr[@class='ant-table-row ant-table-row-level-0'][1]/td[1]")
        borrow = self.driver.instance.find_element_by_xpath("//tr[@class='ant-table-row ant-table-row-level-0'][1]/td[2]")
        repayment = self.driver.instance.find_element_by_xpath("//tr[@class='ant-table-row ant-table-row-level-0'][1]/td[3]")

        assert "Byron Hansen" in name.text
        assert "328" in borrow.text
        assert "109" in repayment.text


        WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_element_located((
                By.XPATH, "//th[@class='ant-table-column-has-actions ant-table-column-has-sorters ant-table-column-sort']"))).click()

        name = self.driver.instance.find_element_by_xpath("//tr[@class='ant-table-row ant-table-row-level-0'][1]/td[1]")
        borrow = self.driver.instance.find_element_by_xpath(
            "//tr[@class='ant-table-row ant-table-row-level-0'][1]/td[2]")
        repayment = self.driver.instance.find_element_by_xpath(
            "//tr[@class='ant-table-row ant-table-row-level-0'][1]/td[3]")

        assert "John Brown" in name.text
        assert "10" in borrow.text
        assert "33" in repayment.text


    def validate_pagination(self):
        self.page("Page 1")
        WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_element_located((
                By.XPATH, "//li[@class='ant-pagination-item ant-pagination-item-2']"))).click()


        nextPage = self.driver.instance.find_element_by_xpath("//li[@title='Next Page']")

        assert nextPage.is_enabled()


    def validade_click_button_swith(self):
        self.page("Page 2")
        self.radioButton("Horizontal")
        WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_element_located((
                By.XPATH, "//div[@class='ant-form-item-control']//button"))).click()
        button = self.driver.instance.find_element_by_xpath(
            "//span[@class='ant-form-item-children']")

        assert button.is_enabled()