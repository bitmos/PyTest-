from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.common.by import By
import time


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestHubSpot(BaseTest):
    @pytest.mark.parametrize("username, password",
                             [
                                 ("admin@gmail.com", "admin123"),
                                 ("shravan@gmail.com", "shravan123"),
                             ]
                             )
    def test_login(self, username, password):
        """
        this method is used to login to hubspot
        :param username:
        :param password:
        :return:
        """
        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element_by_id("username").send.keys(username)
        time.sleep(5)
        self.driver.find_element_by_id("password").send.keys(password)
        time.sleep(5)
