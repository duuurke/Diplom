from selenium import webdriver
from selenium.webdriver.common.by import By

class Kino:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.kinopoisk.ru/?utm_referrer=www.yandex.ru')

    def search(self, value, film_id):
        self.driver.find_element(By.NAME, "kp_query").send_keys(value)
        self.driver.find_element(By.ID, film_id).click()
        return self.driver.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text
