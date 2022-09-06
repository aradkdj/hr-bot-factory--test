from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=list[schemas.Card])
def get_cards(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 0  # noqa: B008
) -> Any:
    """
    Retrieve cards.
    """
    cards = crud.card.get_multi(db, skip=skip, limit=limit)
    return cards


@router.get("/{id}", response_model=schemas.Card)
def get_card(*, db: Session = Depends(deps.get_db), id: int) -> Any:  # noqa: B008
    """
    Get card by ID.
    """
    card = crud.card.get(db=db, id=id)
    if not card:
        raise HTTPException(status_code=404, detail="card not found")
    return card


@router.delete("/{id}", response_model=schemas.Card)
def delete_card(*, db: Session = Depends(deps.get_db), id: int) -> Any:  # noqa: B008
    """
    Delete card.
    """
    card = crud.card.get(db=db, id=id)
    if not card:
        raise HTTPException(status_code=404, detail="card not found")
    card = crud.card.remove(db=db, id=id)
    return card
