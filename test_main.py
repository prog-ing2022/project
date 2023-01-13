from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_simple_russian_text():
    response = client.post(
        "/",
        json={"txt": "у Петрова Коли очень сильно болят ноги"},
    )
    assert response.status_code == 200
    assert response.json() == {"Петрова Коли": {"first": "Коли", "last": "Петрова"}}

def test_long_russian_text():
    response = client.post(
        "/",
        json={"txt": "Добрый день, Галина Петровна! Прошу выполнить заявку Прокина Николая Владимировича от 31.05.2020 и предоставить необходимые доступы следующим сотрудникам: Бирякову Алексею Александровичу, Носовой Анне Сергеевне. Спасибо."},
    )
    assert response.status_code == 200
    assert response.json() == {"Галина Петровна": {"first": "Галина", "last": "Петровна"},
                               "Бирякову Алексею Александровичу": {"first": "Алексею", "last": "Бирякову",
                                                                   "middle": "Александровичу"},
                               "Носовой Анне Сергеевне": {"first": "Анне", "last": "Носовой", "middle": "Сергеевне"}}
def test_only_name_russian_text():
    response = client.post(
        "/",
        json={"txt": "Зубенко Михаил Петрович"},
    )
    assert response.status_code == 200
    assert response.json() == {"Зубенко Михаил Петрович":{"first":"Михаил","last":"Зубенко","middle":"Петрович"}}

def test_no_name_russian_text():
    response = client.post(
        "/",
        json={"txt": "Привет как дела? Я очень люблю машинное обучение"},
    )
    assert response.status_code == 200
    assert response.json() == {}

def test_english_text():
    response = client.post(
        "/",
        json={"txt": "The official YouTube channel for musician, author, artist and peace activist, John Lennon"},
    )
    assert response.status_code == 200
    assert response.json() == {}

