from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.way import WayCreate
from app.tests.utils.text_message import create_random_text_message
from app.tests.utils.utils import random_lower_string


def create_random_way(db: Session) -> models.Way:
    origin_message = create_random_text_message(db)
    destination_message = create_random_text_message(db)
    condition = random_lower_string()
    way_in = WayCreate(
        origin_message_id=origin_message.id,
        destination_message_id=destination_message.id,
        condition=condition,
    )
    return crud.way.create(db=db, obj_in=way_in)
