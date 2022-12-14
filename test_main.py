from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("?text=Добрый день, Галина Петровна! Прошу выполнить заявку Прокина Николая Владимировича от 31.05.2020 и предоставить необходимые доступы следующим сотрудникам: Бирякову Алексею Александровичу, Носовой Анне Сергеевне. Спасибо.")
    assert response.status_code == 200
    assert response.json() == {"msg":{"Галина Петровна":{"first":"Галина","last":"Петровна"},"Бирякову Алексею Александровичу":{"first":"Алексею","last":"Бирякову","middle":"Александровичу"},"Носовой Анне Сергеевне":{"first":"Анне","last":"Носовой","middle":"Сергеевне"}}}