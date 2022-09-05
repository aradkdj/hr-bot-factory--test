from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.message_button import MessageButton
from app.schemas.message_button import MessageButtonCreate, MessageButtonUpdate


class CRUDMessageButton(
    CRUDBase[MessageButton, MessageButtonCreate, MessageButtonUpdate]
):
    def create_with_message(
        self, db: Session, *, obj_in: MessageButtonCreate, message_id: int
    ) -> MessageButton:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, message_id=message_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


message_button = CRUDMessageButton(MessageButton)
