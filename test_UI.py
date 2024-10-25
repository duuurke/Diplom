import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(100)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_in_Cyrillic(chrome_browser):
    with allure.step('кликнуть по строке поиска и ввести название фильма'):
        chrome_browser.get('https://www.kinopoisk.ru/?utm_referrer=www.yandex.ru')
        chrome_browser.find_element(By.NAME, "kp_query").send_keys("поймай")
        chrome_browser.find_element(By.ID, 'suggest-item-film-324').click()
        assert (chrome_browser.find_element(By.CSS_SELECTOR,"span[data-tid='75209b22']").text
                == "Поймай меня, если сможешь (2002)")

def test_in_English(chrome_browser):
    with allure.step('кликнуть по строке поиска и ввести название фильма на английском'):
        chrome_browser.get('https://www.kinopoisk.ru/?utm_referrer=www.yandex.ru')
        chrome_browser.find_element(By.NAME, "kp_query").send_keys("Catch")
        chrome_browser.find_element(By.ID, 'suggest-item-film-324').click()
        assert chrome_browser.find_element(By.CSS_SELECTOR,"span[data-tid='eb6be89']").text == "Catch Me If You Can"

def test_Actor_Search(chrome_browser):
    with allure.step('кликнуть по строке поиска и ввести название Актера'):
        chrome_browser.get('https://www.kinopoisk.ru/?utm_referrer=www.yandex.ru')
        chrome_browser.find_element(By.NAME, "kp_query").send_keys("трамп")
        chrome_browser.find_element(By.ID, 'suggest-item-person-39272').click()
        assert chrome_browser.find_element(By.CSS_SELECTOR,"h1[data-tid='f22e0093']").text == "Дональд Трамп"



def test_authorization(chrome_browser):
    with allure.step('Пройти авторизацию на сайте, ввести пароль и логин'):
        chrome_browser.get('https://www.kinopoisk.ru/?utm_referrer=www.yandex.ru')
        chrome_browser.find_element(By.CSS_SELECTOR,"button[class='styles_loginButton__LWZQp']").click()
        chrome_browser.find_element(By.ID, 'passp-field-login').send_keys('frankorot7@gmail.com')
        chrome_browser.find_element(By.ID, 'passp:sign-in').click()
        chrome_browser.find_element(By.ID, 'passp-field-passwd').send_keys('goptrsGB5J2CL5VZ250B56')
        chrome_browser.find_element(By.ID, 'passp:sign-in').click()
        re = requests.get('https://www.kinopoisk.ru/?utm_referrer=www.yandex.ru')
        assert re.status_code == 200

def test_movies_tab(chrome_browser):
    with (allure.step('кликнуть по кнопке "популярные фильмы"')):
        chrome_browser.get('https://www.kinopoisk.ru/lists/categories/movies/1/')
        chrome_browser.find_element(By.XPATH, f"//span[text() = 'Популярные фильмы']").click()
        assert  chrome_browser.find_element(By.CSS_SELECTOR, "h1[class='styles_title__jB8AZ']"
                                            ).text == 'Популярные фильмы'

