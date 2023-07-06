import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser_web():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--user-data-dir=C:/Users/landa.DESKTOP-GJ08DGE/AppData/Local/Google/Chrome/User Data/")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def login_all_pets(browser_web):
    """Страница 'Все питомцы'"""
    browser_web.get('https://petfriends.skillfactory.ru/')
    browser_web.implicitly_wait(3)

    browser_web.find_element(By.CLASS_NAME, 'btn.btn-success').click()
    browser_web.find_element(By.XPATH, '/html/body/div/div/form/div[4]/a').click()
    browser_web.find_element(By.ID, "email").send_keys("log")
    browser_web.find_element(By.ID, "pass").send_keys("pass")
    browser_web.find_element(By.XPATH, "/html/body/div/div/form/div[3]/button").click()
    return browser_web


@pytest.fixture
def login_my_pets(login_all_pets):
    """Страница 'Мои питомцы'"""
    browser_web.implicitly_wait(3)
    login_all_pets.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    return login_all_pets
