import pytest
from selenium import webdriver


@pytest.fixture
def browser_web():
    options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # options.add_argument("--user-data-dir=C:/Users/landa.DESKTOP-GJ08DGE/AppData/Local/Google/Chrome/User Data/")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

