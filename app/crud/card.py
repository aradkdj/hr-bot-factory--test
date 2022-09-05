from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.card import Card
from app.schemas.card import CardCreate, CardUpdate


class CRUDCard(CRUDBase[Card, CardCreate, CardUpdate]):
    def create_with_message(
        self, db: Session, *, obj_in: CardCreate, message_id: int
    ) -> Card:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, message_id=message_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


card = CRUDCard(Card)
