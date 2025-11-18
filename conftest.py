import pytest
from selenium import  webdriver

@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get('http://automationexercise.com')
    yield driver
    driver.quit()


