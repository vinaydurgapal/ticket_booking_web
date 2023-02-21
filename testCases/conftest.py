import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup():
    s_obj = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s_obj)
    print("launching Browser....................................")
    return driver



