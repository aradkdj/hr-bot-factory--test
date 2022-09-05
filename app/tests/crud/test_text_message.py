from sqlalchemy.orm import Session

from app import crud
from app.schemas.text_message import TextMessageCreate, TextMessageUpdate
from app.tests.utils.utils import random_lower_string, random_placekitten_url


def test_create_text_message(db: Session) -> None:
    response = random_lower_string()
    image = random_placekitten_url()
    text_message_in = TextMessageCreate(response=response, image=image)
    text_message = crud.text_message.create(db=db, obj_in=text_message_in)
    assert text_message.response == response
    assert text_message.image == image


def test_get_text_message(db: Session) -> None:
    response = random_lower_string()
    image = random_placekitten_url()
    text_message_in = TextMessageCreate(response=response, image=image)
    text_message = crud.text_message.create(db=db, obj_in=text_message_in)
    stored_text_message = crud.text_message.get(db=db, id=text_message.id)
    assert stored_text_message
    assert text_message.id == stored_text_message.id
    assert text_message.response == stored_text_message.response
    assert text_message.image == stored_text_message.image


def test_update_text_message(db: Session) -> None:
    response = random_lower_string()
    image = random_placekitten_url()
    text_message_in = TextMessageCreate(response=response, image=image)
    text_message = crud.text_message.create(db=db, obj_in=text_message_in)
    response2 = random_lower_string()
    text_message_update = TextMessageUpdate(response=response2)
    text_message2 = crud.text_message.update(
        db=db, db_obj=text_message, obj_in=text_message_update
    )
    assert text_message2.id == text_message.id
    assert text_message2.response == text_message.response
    assert text_message2.image == text_message.image


def test_delete_text_message(db: Session) -> None:
    response = random_lower_string()
    image = random_placekitten_url()
    text_message_in = TextMessageCreate(response=response, image=image)
    text_message = crud.text_message.create(db=db, obj_in=text_message_in)
    text_message2 = crud.text_message.remove(db=db, id=text_message.id)
    text_message3 = crud.text_message.get(db=db, id=text_message.id)
    assert text_message3 is None
    assert text_message2.id == text_message.id
    assert text_message2.response == text_message.response
    assert text_message2.image == text_message.image
