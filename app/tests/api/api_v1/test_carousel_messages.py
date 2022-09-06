from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.carousel_message import create_random_carousel_message


def test_create_carousel_message(client: TestClient, db: Session) -> None:
    carousel_message = {
        "carousel_message_in": {
            "response": "Foo",
        },
        "buttons_for_cards_in": [
            [
                {"text": "Bar", "value": "bar"},
            ],
            [
                {"text": "Baz", "value": "baz"},
            ],
        ],
        "cards_in": [
            {"image": "https://placekitten.com/200/300", "text": "Crux"},
            {"image": "https://placekitten.com/300/400", "text": "Monty"},
        ],
    }
    response = client.post(
        f"{settings.API_V1_STR}/messages/carousel/", json=carousel_message
    )
    assert response.status_code == 200
    content = response.json()
    assert content["response"] == carousel_message["carousel_message_in"]["response"]
    assert "id" in content
    assert len(content["cards"]) == len(carousel_message["cards_in"])
    assert all("id" in card for card in content["cards"])
    assert all(
        a["text"] == b["text"] and a["image"] == b["image"]
        for (a, b) in zip(content["cards"], carousel_message["cards_in"])
    )
    assert all(
        "id" in button for cards in content["cards"] for button in cards["buttons"]
    )
    assert all(
        a["text"] == b["text"] and a["value"] == b["value"]
        for (a, b) in zip(
            [button for card in content["cards"] for button in card["buttons"]],
            [
                button
                for buttons_for_card in carousel_message["buttons_for_cards_in"]
                for button in buttons_for_card
            ],
        )
    )


def test_read_carousel_message(client: TestClient, db: Session) -> None:
    carousel_message = create_random_carousel_message(db)
    response = client.get(
        f"{settings.API_V1_STR}/messages/carousel/{carousel_message.id}"
    )
    assert response.status_code == 200
    content = response.json()
    assert content["response"] == carousel_message.response
    assert content["id"] == carousel_message.id
    assert len(content["cards"]) == len(carousel_message.cards)
    assert all(card["id"] for card in content["cards"])
    assert all(
        a["text"] == b.text and a["image"] == b.image
        for (a, b) in zip(content["cards"], carousel_message.cards)
    )
    assert all(
        a["id"] == b.id
        for (a, b) in zip(
            [button for card in content["cards"] for button in card["buttons"]],
            [button for card in carousel_message.cards for button in card.buttons],
        )
    )
    assert all(
        a["text"] == b.text and a["value"] == b.value
        for (a, b) in zip(
            [button for card in content["cards"] for button in card["buttons"]],
            [button for card in carousel_message.cards for button in card.buttons],
        )
    )
