from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.button_message import create_random_button_message


def test_create_button_message(client: TestClient, db: Session) -> None:
    button_message = {
        "button_message_in": {
            "response": "Foo",
            "image": "https://placekitten.com/200/300",
        },
        "message_buttons_in": [
            {"text": "Bar", "value": "bar"},
            {"text": "Baz", "value": "baz"},
        ],
    }

    response = client.post(
        f"{settings.API_V1_STR}/messages/button/", json=button_message
    )
    assert response.status_code == 200
    content = response.json()
    assert content["response"] == button_message["button_message_in"]["response"]
    assert content["image"] == button_message["button_message_in"]["image"]
    assert "id" in content
    assert len(content["buttons"]) == len(button_message["message_buttons_in"])
    assert all("id" in button for button in content["buttons"])
    assert all(
        a["text"] == b["text"] and a["value"] == b["value"]
        for (a, b) in zip(content["buttons"], button_message["message_buttons_in"])
    )


def test_read_button_message(client: TestClient, db: Session) -> None:
    button_message = create_random_button_message(db)
    response = client.get(f"{settings.API_V1_STR}/messages/button/{button_message.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["response"] == button_message.response
    assert content["id"] == button_message.id
    assert len(content["buttons"]) == len(button_message.buttons)
    assert all(
        a["id"] == b.id for (a, b) in zip(content["buttons"], button_message.buttons)
    )
    assert all(
        a["text"] == b.text and a["value"] == b.value
        for (a, b) in zip(content["buttons"], button_message.buttons)
    )
