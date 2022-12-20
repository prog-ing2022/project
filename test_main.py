from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("?text=Добрый день, Галина Петровна! Прошу выполнить заявку Прокина Николая Владимировича от 31.05.2020 и предоставить необходимые доступы следующим сотрудникам: Бирякову Алексею Александровичу, Носовой Анне Сергеевне. Спасибо.")
    assert response.status_code == 200
    assert response.json() == {"Галина Петровна":{"first":"Галина","last":"Петровна"},"Бирякову Алексею Александровичу":{"first":"Алексею","last":"Бирякову","middle":"Александровичу"},"Носовой Анне Сергеевне":{"first":"Анне","last":"Носовой","middle":"Сергеевне"}}
    response = client.get("?text=Зубенко Михаил Петрович")
    assert response.status_code == 200
    assert response.json() == {"Зубенко Михаил Петрович":{"first":"Михаил","last":"Зубенко","middle":"Петрович"}}
    response = client.get("?text=у Петрова Коли очень сильно болят ноги")
    assert response.status_code == 200
    assert response.json() == {"Петрова Коли":{"first":"Коли","last":"Петрова"}}
    response = client.get("?text=Привет как дела? Я очень люблю машинное обучение")
    assert response.status_code == 200
    assert response.json() == {}
    response = client.get("?text=Любимая Галина Петровна! Давно хочу рассказать вам о своих чувствах! Ваш Сындыкмаа Шожул.")
    assert response.status_code == 200
    assert response.json() == {"Любимая Галина Петровна":{"first":"Галина","last":"Любимая","middle":"Петровна"}}
    response = client.get("?text=The official YouTube channel for musician, author, artist and peace activist, John Lennon")
    assert response.status_code == 200
    assert response.json() == {}
    assert response.json() == {"msg":{"Галина Петровна":{"first":"Галина","last":"Петровна"},"Бирякову Алексею Александровичу":{"first":"Алексею","last":"Бирякову","middle":"Александровичу"},"Носовой Анне Сергеевне":{"first":"Анне","last":"Носовой","middle":"Сергеевне"}}}
