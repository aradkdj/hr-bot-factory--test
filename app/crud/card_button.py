from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.card_button import CardButton
from app.schemas.card_button import CardButtonCreate, CardButtonUpdate


class CRUDCardButton(CRUDBase[CardButton, CardButtonCreate, CardButtonUpdate]):
    def create_with_card(
        self, db: Session, *, obj_in: CardButtonCreate, card_id: int
    ) -> CardButton:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, card_id=card_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


card_button = CRUDCardButton(CardButton)
