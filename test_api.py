import requests

headers = {'X-API-KEY':'3FBB5PZ-REWMKR2-G5N7WQ0-8JS4FQN'}
url = 'https://api.kinopoisk.dev/v1.4/'

def test_poisk():
    response = requests.get(f"{url}movie/search?page=1&limit=1&query=Поймай меня, если сможешь",
                           headers=headers)
    assert response.status_code == 200

def test_Ac():
    response = requests.get(f"{url}person/search?page=1&limit=1&query=Дональд Трамп",
                           headers=headers)
    assert response.status_code == 200

def test_serial():
    response = requests.get(f"{url}movie/search?page=1&limit=1&query=Силиконовая долина",
                           headers=headers)
    assert response.status_code == 200

def test_movi():
    response = requests.get(f"{url}movie/search?page=1&limit=1&query=Requiem for a Dream",
                           headers=headers)
    assert response.status_code == 200

def test_movi_neg():
    response = requests.get(f"{url}movie/search?page=1&limit=&query=кидзмараули",
                           headers=headers)
    assert response.status_code == 400