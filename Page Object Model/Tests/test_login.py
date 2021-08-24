import pytest

from Config.config import TestData
from Pages.login import LoginPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):
    def test_loginlink(self):
        self.loginpage=LoginPage(self.driver)
        flag= self.loginpage.is_present()
        assert flag

    def test_page_title(self):
        self.loginpage = LoginPage(self.driver)
        title=self.loginpage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title==TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(TestData.USER_NAME,TestData.PASSWORD)