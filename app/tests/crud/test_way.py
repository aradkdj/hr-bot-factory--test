from sqlalchemy.orm import Session

from app import crud
from app.schemas.way import WayCreate, WayUpdate
from app.tests.utils.text_message import create_random_text_message
from app.tests.utils.utils import random_lower_string


def test_create_way(db: Session) -> None:
    origin_message = create_random_text_message(db=db)
    destination_message = create_random_text_message(db)
    condition = random_lower_string()
    way_in = WayCreate(
        origin_message_id=origin_message.id,
        destination_message_id=destination_message.id,
        condition=condition,
    )
    way = crud.way.create(db=db, obj_in=way_in)
    assert way.origin_message_id == way_in.origin_message_id
    assert way.destination_message_id == way_in.destination_message_id
    assert way.condition == way_in.condition


def test_get_way(db: Session) -> None:
    origin_message = create_random_text_message(db=db)
    destination_message = create_random_text_message(db)
    condition = random_lower_string()
    way_in = WayCreate(
        origin_message_id=origin_message.id,
        destination_message_id=destination_message.id,
        condition=condition,
    )
    way = crud.way.create(db=db, obj_in=way_in)
    stored_way = crud.way.get(db=db, id=way.id)
    assert stored_way
    assert way.id == stored_way.id
    assert way.origin_message_id == stored_way.origin_message_id
    assert way.destination_message_id == stored_way.destination_message_id
    assert way.condition == stored_way.condition


def test_update_way(db: Session) -> None:
    origin_message = create_random_text_message(db)
    destination_message = create_random_text_message(db)
    condition = random_lower_string()
    way_in = WayCreate(
        origin_message_id=origin_message.id,
        destination_message_id=destination_message.id,
        condition=condition,
    )
    way = crud.way.create(db=db, obj_in=way_in)
    destination_message2 = create_random_text_message(db)
    way_update = WayUpdate(destination_message_id=destination_message2.id)
    way2 = crud.way.update(db=db, db_obj=way, obj_in=way_update)
    assert way.id == way2.id
    assert way.origin_message_id == way2.origin_message_id
    assert way.destination_message_id == way2.destination_message_id
    assert way.condition == way2.condition


def test_delete_way(db: Session) -> None:
    origin_message = create_random_text_message(db)
    destination_message = create_random_text_message(db)
    condition = random_lower_string()
    way_in = WayCreate(
        origin_message_id=origin_message.id,
        destination_message_id=destination_message.id,
        condition=condition,
    )
    way = crud.way.create(db=db, obj_in=way_in)
    way2 = crud.way.remove(db=db, id=way.id)
    way3 = crud.way.get(db=db, id=way.id)
    assert way3 is None
    assert way2.id == way.id
    assert way2.origin_message_id == way.origin_message_id
    assert way2.destination_message_id == way.destination_message_id
    assert way2.condition == way.condition
