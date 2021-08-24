from selenium import webdriver
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Config.config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == 'chrome':
        web_driver = webdriver.Chrome(ChromeDriverManager().install())

    # if request.param == 'firefox':
    #     a
#web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


    request.cls.driver = web_driver

    yield
    web_driver.close()
