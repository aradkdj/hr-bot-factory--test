from typing import Any

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.card import CardCreate
from app.schemas.card_button import CardButtonCreate
from app.schemas.carousel_message import CarouselMessageCreate
from app.tests.utils.utils import random_lower_string, random_placekitten_url


def create_random_carousel_message(db: Session) -> models.CarouselMessage:
    response = random_lower_string()
    cards = [
        {
            "image": random_placekitten_url(),
            "text": random_lower_string(),
        }
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

    return carousel_message
