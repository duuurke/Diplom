import requests
import allure

headers = {'X-API-KEY':'3FBB5PZ-REWMKR2-G5N7WQ0-8JS4FQN'}
url = 'https://api.kinopoisk.dev/v1.4/'

def test_poisk():
    with allure.step('поиск названия фильма на кириллице'):
        response = requests.get(f"{url}movie/search?page=1&limit=1&query=Поймай меня, если сможешь",
                                headers=headers)
        assert response.status_code == 200

def test_Ac():
    with allure.step('поиск актера на кириллице'):
        response = requests.get(f"{url}person/search?page=1&limit=1&query=Дональд Трамп",
                                headers=headers)
        assert response.status_code == 200

def test_serial():
    with allure.step('поиск сериала на кириллице'):
        response = requests.get(f"{url}movie/search?page=1&limit=1&query=Силиконовая долина",
                                headers=headers)
        assert response.status_code == 200

def test_movi():
    with allure.step('поиск названия фильма на английском языке'):
        response = requests.get(f"{url}movie/search?page=1&limit=1&query=Requiem for a Dream",
                                headers=headers)
        assert response.status_code == 200

def test_movi_neg():
    with allure.step('поиск не существующего фильма'):
        response = requests.get(f"{url}movie/search?page=1&limit=&query=кидзмараули",
                                headers=headers)
        assert response.status_code == 400