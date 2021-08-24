from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    EMAIL= (By.NAME,'email')
    PASSWORD = (By.NAME, 'password')
    LOGIN = (By.TAG_NAME, 'button')

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    def get_login_page_title(self,title):
        return self.get_title(title)

    def do_login(self,username,password):
        self.do_send(self.EMAIL,username)
        self.do_send(self.PASSWORD,password)
        self.do_click(self.LOGIN)


    def is_present(self):
        return self.is_enabled(self.LOGIN)