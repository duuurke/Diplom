import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(100)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_G(chrome_browser):
    chrome_browser.get('https://www.kinopoisk.ru/?utm_referrer=www.yandex.ru')
    chrome_browser.find_element(By.NAME, "kp_query").send_keys("поймай")
    chrome_browser.find_element(By.ID, 'suggest-item-film-324').click()
    assert chrome_browser.find_element(By.CSS_SELECTOR,"span[data-tid='75209b22']").text == "Поймай меня, если сможешь (2002)"

def test_G(chrome_browser):
    chrome_browser.get('https://www.kinopoisk.ru/?utm_referrer=www.yandex.ru')
    chrome_browser.find_element(By.NAME, "kp_query").send_keys("Catch")
    chrome_browser.find_element(By.ID, 'suggest-item-film-324').click()
    assert chrome_browser.find_element(By.CSS_SELECTOR,"span[data-tid='eb6be89']").text == "Catch Me If You Can"


