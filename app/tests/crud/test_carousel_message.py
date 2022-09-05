from typing import Any

from sqlalchemy.orm import Session

from app import crud
from app.schemas.card import CardCreate
from app.schemas.card_button import CardButtonCreate
from app.schemas.carousel_message import CarouselMessageCreate, CarouselMessageUpdate
from app.tests.utils.utils import random_lower_string, random_placekitten_url


def test_create_carousel_message(db: Session) -> None:
    response = random_lower_string()
    cards = [
        {"image": random_placekitten_url(), "text": random_lower_string()}
        for _ in range(2)
    ]
    cards_buttons = [
        [
            {"text": random_lower_string(), "value": random_lower_string()}
            for __ in range(2)
        ]
        for _ in range(2)
    ]
    carousel_message_in = CarouselMessageCreate(response=response)
    carousel_message = crud.carousel_message.create(db=db, obj_in=carousel_message_in)
    card_api: dict[str, Any]
    card_buttons: list[dict[str, Any]]
    for (card_api, card_buttons) in zip(cards, cards_buttons):
        card_in = CardCreate(**card_api)
        card = crud.card.create_with_message(
            db=db, obj_in=card_in, message_id=carousel_message.id
        )
        for button in card_buttons:
            button_in = CardButtonCreate(**button)
            crud.card_button.create_with_card(db=db, obj_in=button_in, card_id=card.id)
    assert carousel_message.response == response
    assert len(carousel_message.cards) == len(cards)
    assert all(
        a.text == b["text"] and a.image == b["image"]
        for (a, b) in zip(carousel_message.cards, cards)
    )
    assert all(
        a.text == b["text"] and a.value == b["value"]
        for (a, b) in zip(
            [button for card in carousel_message.cards for button in card.buttons],
            [button for card_buttons in cards_buttons for button in card_buttons],
        )
    )


def test_get_carousel_message(db: Session) -> None:
    response = random_lower_string()
    cards = [
        {"image": random_placekitten_url(), "text": random_lower_string()}
        for _ in range(2)
    ]
    cards_buttons = [
        [
            {"text": random_lower_string(), "value": random_lower_string()}
            for __ in range(2)
        ]
        for _ in range(2)
    ]
    carousel_message_in = CarouselMessageCreate(response=response)
    carousel_message = crud.carousel_message.create(db=db, obj_in=carousel_message_in)
    card_api: dict[str, Any]
    card_buttons: list[dict[str, Any]]
    for (card_api, card_buttons) in zip(cards, cards_buttons):
        card_in = CardCreate(**card_api)
        card = crud.card.create_with_message(
            db=db, obj_in=card_in, message_id=carousel_message.id
        )
        for button in card_buttons:
            button_in = CardButtonCreate(**button)
            crud.card_button.create_with_card(db=db, obj_in=button_in, card_id=card.id)
    stored_carousel_message = crud.carousel_message.get(db=db, id=carousel_message.id)
    assert stored_carousel_message
    assert carousel_message.id == stored_carousel_message.id
    assert carousel_message.response == stored_carousel_message.response
    assert len(stored_carousel_message.cards) == len(carousel_message.cards)
    assert all(
        a.text == b.text and a.image == b.image
        for (a, b) in zip(stored_carousel_message.cards, carousel_message.cards)
    )
    assert all(
        a.text == b.text and a.value == b.value
        for (a, b) in zip(
            [
                button
                for card in stored_carousel_message.cards
                for button in card.buttons
            ],
            [button for card in carousel_message.cards for button in card.buttons],
        )
    )


def test_update_carousel_message(db: Session) -> None:
    response = random_lower_string()
    cards = [
        {"image": random_placekitten_url(), "text": random_lower_string()}
        for _ in range(2)
    ]
    cards_buttons = [
        [
            {"text": random_lower_string(), "value": random_lower_string()}
            for __ in range(2)
        ]
        for _ in range(2)
    ]
    carousel_message_in = CarouselMessageCreate(response=response)
    carousel_message = crud.carousel_message.create(db=db, obj_in=carousel_message_in)
    card_api: dict[str, Any]
    card_buttons: list[dict[str, Any]]
    for (card_api, card_buttons) in zip(cards, cards_buttons):
        card_in = CardCreate(**card_api)
        card = crud.card.create_with_message(
            db=db, obj_in=card_in, message_id=carousel_message.id
        )
        for button in card_buttons:
            button_in = CardButtonCreate(**button)
            crud.card_button.create_with_card(db=db, obj_in=button_in, card_id=card.id)
    response2 = random_lower_string()
    cards2 = [
        {"image": random_placekitten_url(), "text": random_lower_string()}
        for _ in range(3)
    ]
    cards_buttons2 = [
        [
            {"text": random_lower_string(), "value": random_lower_string()}
            for __ in range(3)
        ]
        for _ in range(3)
    ]
    carousel_message_update = CarouselMessageUpdate(response=response2)
    carousel_message2 = crud.carousel_message.update(
        db=db, db_obj=carousel_message, obj_in=carousel_message_update
    )
    card_api2: dict[str, Any]
    card_buttons2: list[dict[str, Any]]
    for (card_api2, card_buttons2) in zip(cards2, cards_buttons2):
        card_in = CardCreate(**card_api2)
        card = crud.card.create_with_message(
            db=db, obj_in=card_in, message_id=carousel_message2.id
        )
        for button in card_buttons2:
            button_in = CardButtonCreate(**button)
            crud.card_button.create_with_card(db=db, obj_in=button_in, card_id=card.id)


def test_delete_carousel_message(db: Session) -> None:
    response = random_lower_string()
    cards = [
        {"image": random_placekitten_url(), "text": random_lower_string()}
        for _ in range(2)
    ]
    cards_buttons = [
        [
            {"text": random_lower_string(), "value": random_lower_string()}
            for __ in range(2)
        ]
        for _ in range(2)
    ]
    carousel_message_in = CarouselMessageCreate(response=response)
    carousel_message = crud.carousel_message.create(db=db, obj_in=carousel_message_in)
    card_api: dict[str, Any]
    card_buttons: list[dict[str, Any]]
    for (card_api, card_buttons) in zip(cards, cards_buttons):
        card_in = CardCreate(**card_api)
        card = crud.card.create_with_message(
            db=db, obj_in=card_in, message_id=carousel_message.id
        )
        for button in card_buttons:
            button_in = CardButtonCreate(**button)
            crud.card_button.create_with_card(db=db, obj_in=button_in, card_id=card.id)
    carousel_message2 = crud.carousel_message.remove(db=db, id=carousel_message.id)
    carousel_message3 = crud.carousel_message.get(db=db, id=carousel_message.id)
    assert carousel_message3 is None
    assert carousel_message2.id == carousel_message.id
    assert carousel_message2.response == carousel_message.response
    assert len(carousel_message2.cards) == len(carousel_message.cards)
    assert all(
        a.text == b.text and a.image == b.image
        for (a, b) in zip(carousel_message2.cards, carousel_message.cards)
    )
    assert all(
        a.text == b.text and a.value == b.value
        for (a, b) in zip(
            [button for card in carousel_message2.cards for button in card.buttons],
            [button for card in carousel_message.cards for button in card.buttons],
        )
    )
