import pytest
import requests
import allure

headers = {'X-API-KEY':'3FBB5PZ-REWMKR2-G5N7WQ0-8JS4FQN'}
url = 'https://api.kinopoisk.dev/v1.4/'

@allure.title('Функционал поисковой строки на сайте kinopoisk при поиске фильма')
@allure.description('находим фильм на кириллице через поисковую строку')
@allure.severity('1')
@pytest.mark.parametrize('film', [
    "поймай меня если сможешь",
    'мгла'
    ])
def test_poisk(film):
    with allure.step('поиск фильма на кириллице и убеждаемся что код равен 200'):
        response = requests.get(f"{url}movie/search?page=1&limit=1&query={film}",
                                headers=headers)
        assert response.status_code == 200

@allure.title('Функционал поисковой строки на сайте kinopoisk при поиске актера')
@allure.description('находим актера на кириллице через поисковую строку')
@allure.severity('1')
@pytest.mark.parametrize('actor', [
    "Дональд Трамп",
    'Рэйчел Элиг'
    ])
def test_ac(actor):
    with allure.step('поиск актера на кириллице и убеждаемся что код равен 200'):
        response = requests.get(f"{url}person/search?page=1&limit=1&query={actor}",
                                headers=headers)
        assert response.status_code == 200

@allure.title('Функционал поисковой строки на сайта kinopoisk при поиске сериала')
@allure.description('находим сериал на кириллице через поисковую строку')
@allure.severity('1')
@pytest.mark.parametrize('serials', [
    "Силиконовая долина",
    'озорк'
    ])
def test_serial(serials):
    with allure.step('поиск сериала на кириллице и убеждаемся что код равен 200'):
        response = requests.get(f"{url}movie/search?page=1&limit=1&query={serials}",
                                headers=headers)
        assert response.status_code == 200

@allure.title('Функционал поисковой строки на сайте kinopoisk при поиске фильма на другом языке')
@allure.description('находим фильм на английском языке через поисковую строку')
@allure.severity('1')
@pytest.mark.parametrize('film_eng', [
    "Requiem for a Dream",
    'Mr. Robot'
    ])
def test_movi(film_eng):
    with allure.step('поиск фильма на английском и убеждаемся что код равен 200'):
        response = requests.get(f"{url}movie/search?page=1&limit=1&query={film_eng}",
                                headers=headers)
        assert response.status_code == 200

@allure.title('Функционал поисковой строки на сайте kinopoisk при поиске несуществующего значения')
@allure.description('пытаемся найти несуществующее значение через поисковую строку')
@allure.severity('1')
@pytest.mark.parametrize('non_existent', [
        "кидзмараули",
        'osio'
        'oiso'
    ])
def test_non_movi(non_existent):
    with allure.step('поиск не существующий фильм и убедится что код равен 200'):
        response = requests.get(f"{url}movie/search?page=1&limit=&query={non_existent}",
                                headers=headers)
        assert response.status_code == 400