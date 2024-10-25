import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from kino_class import Kino

@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(100)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title('проверить функционал поисковой строки на сайте kinopoisk при поиске фильма')
@allure.description('тестируем поисковую систему сайта на поиск фильма на кириллице')
@allure.severity('1')
def test_in_cyrillic(chrome_browser):
    with allure.step(
            'кликнуть по строке поиска, ввести название фильма в поле, нажать поиск и убедиться что результат верен'):
        kino = Kino(chrome_browser)
        assert kino.search('поймай', 'suggest-item-film-324') == "Поймай меня, если сможешь (2002)"

@allure.title('Проверить функционал поисковой строки на сайте kinopoisk при поиске фильма на английском языке')
@allure.description('тестируем поисковую систему сайта на поиск фильма на английском языке')
@allure.severity('1')
def test_in_english(chrome_browser):
    with (allure.step(
            'кликнуть по строке поиска, ввести название фильма в поле на английском языке, '
            'нажать поиск и убедиться что результат верен')):
        chrome_browser.get('https://www.kinopoisk.ru/?utm_referrer=www.yandex.ru')
        chrome_browser.find_element(By.NAME, "kp_query").send_keys("Catch")
        chrome_browser.find_element(By.ID, 'suggest-item-film-324').click()
        assert chrome_browser.find_element(By.CSS_SELECTOR,"span[data-tid='eb6be89']"
                                           ).text == "Catch Me If You Can"

@allure.title('Проверить функционал поисковой строки на сайте kinopoisk при поиске актера ')
@allure.description('тестируем поисковую систему сайта на поиск актера')
@allure.severity('1')
def test_actor_Search(chrome_browser):
    with allure.step(
            'кликнуть по строке поиска, ввести имя актера в поле, нажать поиск и убедиться что результат верен'):
        chrome_browser.get('https://www.kinopoisk.ru/?utm_referrer=www.yandex.ru')
        chrome_browser.find_element(By.NAME, "kp_query").send_keys("трамп")
        chrome_browser.find_element(By.ID, 'suggest-item-person-39272').click()
        assert chrome_browser.find_element(By.CSS_SELECTOR,"h1[data-tid='f22e0093']").text == "Дональд Трамп"


@allure.title('Авторизоваться на сайте kinopoisk ')
@allure.description('пройти авторизацию на сайте при помощи логина и пароля')
@allure.severity('1')
def test_authorization(chrome_browser):
    with allure.step(
            'кликнуть на кнопку "вход" ввести пароль и логин нажать продолжить и убедится что результат успешен'):
        chrome_browser.get('https://www.kinopoisk.ru/?utm_referrer=www.yandex.ru')
        chrome_browser.find_element(By.CSS_SELECTOR,"button[class='styles_loginButton__LWZQp']").click()
        chrome_browser.find_element(By.ID, 'passp-field-login').send_keys('frankorot7@gmail.com')
        chrome_browser.find_element(By.ID, 'passp:sign-in').click()
        chrome_browser.find_element(By.ID, 'passp-field-passwd').send_keys('goptrsGB5J2CL5VZ250B56')
        chrome_browser.find_element(By.ID, 'passp:sign-in').click()
        current_url = chrome_browser.current_url
        assert 'https://passport.yandex.ru/auth/welcome' in current_url

@allure.title('пройти в нужный раздел по клику')
@allure.description('пройти в раздел "популярные фильмы" кликнув на кнопку и убедится что результат успешен')
@allure.severity('1')
def test_movies_tab(chrome_browser):
    with (allure.step('кликнуть по кнопке "популярные фильмы"')):
        chrome_browser.get('https://www.kinopoisk.ru/lists/categories/movies/1/')
        chrome_browser.find_element(By.XPATH, f"//span[text() = 'Популярные фильмы']").click()
        assert  chrome_browser.find_element(By.CSS_SELECTOR, "h1[class='styles_title__jB8AZ']"
                                            ).text == 'Популярные фильмы'

