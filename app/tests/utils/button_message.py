from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.button_message import ButtonMessageCreate
from app.schemas.message_button import MessageButtonCreate
from app.tests.utils.utils import random_lower_string, random_placekitten_url


def create_random_button_message(db: Session) -> models.ButtonMessage:
    response = random_lower_string()
    image = random_placekitten_url()
    buttons = [
        {"text": random_lower_string(), "value": random_lower_string()}
        for _ in range(2)
    ]
    button_message_in = ButtonMessageCreate(response=response, image=image)
    button_message = crud.button_message.create(db=db, obj_in=button_message_in)
    for button in buttons:
        crud.message_button.create_with_message(
            db=db,
            obj_in=MessageButtonCreate.parse_obj(button),
            message_id=button_message.id,
        )

    return button_message
