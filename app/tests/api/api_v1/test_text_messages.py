from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.text_message import create_random_text_message


def test_create_text_message(client: TestClient, db: Session) -> None:
    text_message = {"response": "Foo", "image": "https://placekitten.com/200/300"}
    response = client.post(f"{settings.API_V1_STR}/messages/text/", json=text_message)
    assert response.status_code == 200
    content = response.json()
    assert content["response"] == text_message["response"]
    assert content["image"] == text_message["image"]
    assert "id" in content


def test_read_text_message(client: TestClient, db: Session) -> None:
    text_message = create_random_text_message(db)
    response = client.get(f"{settings.API_V1_STR}/messages/text/{text_message.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["response"] == text_message.response
    assert content["id"] == text_message.id
