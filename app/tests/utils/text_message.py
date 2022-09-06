from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.text_message import TextMessageCreate
from app.tests.utils.utils import random_lower_string, random_placekitten_url


def create_random_text_message(db: Session) -> models.TextMessage:
    response = random_lower_string()
    image = random_placekitten_url()
    text_message_in = TextMessageCreate(response=response, image=image)
    return crud.text_message.create(db=db, obj_in=text_message_in)
