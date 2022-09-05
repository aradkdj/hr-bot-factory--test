from sqlalchemy.orm import Session

from app import crud
from app.schemas.button_message import ButtonMessageCreate, ButtonMessageUpdate
from app.schemas.message_button import MessageButtonCreate
from app.tests.utils.utils import random_lower_string, random_placekitten_url


def test_create_button_message(db: Session) -> None:
    response = random_lower_string()
    image = random_placekitten_url()
    button_message_in = ButtonMessageCreate(response=response, image=image)
    button_message = crud.button_message.create(db=db, obj_in=button_message_in)
    buttons = [
        {"text": random_lower_string(), "value": random_lower_string()}
        for _ in range(2)
    ]
    for button in buttons:
        crud.message_button.create_with_message(
            db=db, obj_in=MessageButtonCreate(**button), message_id=button_message.id
        )
    assert button_message.response == response
    assert button_message.image == image
    assert len(button_message.buttons) == len(buttons)
    assert all(button.id for button in button_message.buttons)
    assert all(
        a.text == b["text"] and a.value == b["value"]
        for (a, b) in zip(button_message.buttons, buttons)
    )


def test_get_button_message(db: Session) -> None:
    response = random_lower_string()
    image = random_placekitten_url()
    button_message_in = ButtonMessageCreate(response=response, image=image)
    button_message = crud.button_message.create(db=db, obj_in=button_message_in)
    buttons = [
        {"text": random_lower_string(), "value": random_lower_string()}
        for _ in range(2)
    ]
    for button in buttons:
        crud.message_button.create_with_message(
            db=db, obj_in=MessageButtonCreate(**button), message_id=button_message.id
        )
    stored_button_message = crud.button_message.get(db=db, id=button_message.id)
    assert stored_button_message
    assert button_message.id == stored_button_message.id
    assert button_message.image == stored_button_message.image
    assert len(stored_button_message.buttons) == len(button_message.buttons)
    assert all(button.id for button in stored_button_message.buttons)
    assert all(
        a.text == b.text and a.value == b.value
        for (a, b) in zip(stored_button_message.buttons, button_message.buttons)
    )


def test_update_button_message(db: Session) -> None:
    response = random_lower_string()
    image = random_placekitten_url()
    button_message_in = ButtonMessageCreate(response=response, image=image)
    button_message = crud.button_message.create(db=db, obj_in=button_message_in)
    buttons = [
        {"text": random_lower_string(), "value": random_lower_string()}
        for _ in range(2)
    ]
    for button in buttons:
        crud.message_button.create_with_message(
            db=db, obj_in=MessageButtonCreate(**button), message_id=button_message.id
        )
    response2 = random_lower_string()
    button_message_update = ButtonMessageUpdate(response=response2)
    button_message2 = crud.button_message.update(
        db=db, db_obj=button_message, obj_in=button_message_update
    )
    buttons2 = [
        {"text": random_lower_string(), "value": random_lower_string()}
        for _ in range(3)
    ]
    for button in buttons2:
        crud.message_button.create_with_message(
            db=db, obj_in=MessageButtonCreate(**button), message_id=button_message.id
        )
    assert button_message.id == button_message2.id
    assert button_message.response == button_message2.response
    assert button_message.image == button_message2.image
    assert len(button_message.buttons) == len(button_message2.buttons)
    assert all(
        a.text == b.text and a.value == b.value
        for (a, b) in zip(button_message.buttons, button_message2.buttons)
    )


def test_delete_button_message(db: Session) -> None:
    response = random_lower_string()
    image = random_placekitten_url()
    button_message_in = ButtonMessageCreate(response=response, image=image)
    button_message = crud.button_message.create(db=db, obj_in=button_message_in)
    buttons = [
        {"text": random_lower_string(), "value": random_lower_string()}
        for _ in range(2)
    ]
    for button in buttons:
        crud.message_button.create_with_message(
            db=db, obj_in=MessageButtonCreate(**button), message_id=button_message.id
        )
    button_message2 = crud.button_message.remove(db=db, id=button_message.id)
    button_message3 = crud.button_message.get(db=db, id=button_message.id)
    assert button_message3 is None
    assert button_message2.id == button_message.id
    assert button_message2.response == button_message.response
    assert button_message2.image == button_message.image
    assert len(button_message2.buttons) == len(button_message.buttons)
    assert all(
        a.text == b.text and a.value == b.value
        for (a, b) in zip(button_message2.buttons, button_message.buttons)
    )
