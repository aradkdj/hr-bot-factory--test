from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.text_message import create_random_text_message
from app.tests.utils.way import create_random_way


def test_create_way(client: TestClient, db: Session) -> None:
    text_message1 = create_random_text_message(db)
    text_message2 = create_random_text_message(db)
    way = {
        "origin_message_id": text_message1.id,
        "destination_message_id": text_message2.id,
        "condition": "foo",
    }
    response = client.post(f"{settings.API_V1_STR}/ways/", json=way)
    assert response.status_code == 200
    content = response.json()
    assert content["origin_message_id"] == way["origin_message_id"]
    assert content["destination_message_id"] == way["destination_message_id"]
    assert content["condition"] == way["condition"]
    assert "id" in content


def test_read_way(client: TestClient, db: Session) -> None:
    way = create_random_way(db=db)
    response = client.get(f"{settings.API_V1_STR}/ways/{way.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["origin_message_id"] == way.origin_message_id
    assert content["destination_message_id"] == way.destination_message_id
    assert content["condition"] == way.condition
    assert content["id"] == way.id
