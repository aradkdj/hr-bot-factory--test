from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=list[schemas.CarouselMessage])
def read_carousel_messages(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100  # noqa: B008
) -> Any:
    """
    Retrieve carousel messages.
    """
    carousel_messages = crud.carousel_message.get_multi(db=db, skip=skip, limit=limit)
    return carousel_messages


@router.post("/", response_model=schemas.CarouselMessage)
def create_carousel_message(
    *,
    db: Session = Depends(deps.get_db),  # noqa: B008
    carousel_message_in: schemas.CarouselMessageCreate,
    cards_in: list[schemas.CardCreate],
    buttons_for_cards_in: list[list[schemas.CardButtonCreate]]
) -> Any:
    """
    Create new carousel message.
    """
    carousel_message = crud.carousel_message.create(db=db, obj_in=carousel_message_in)
    card_in: schemas.CardCreate
    card_buttons_in: list[schemas.CardButtonCreate]
    for (card_in, card_buttons_in) in zip(cards_in, buttons_for_cards_in):
        card = crud.card.create_with_message(
            db=db, obj_in=card_in, message_id=carousel_message.id
        )
        for card_button_in in card_buttons_in:
            crud.card_button.create_with_card(
                db=db, obj_in=card_button_in, card_id=card.id
            )
    return carousel_message


@router.put("/{id}", response_model=schemas.CarouselMessage)
def update_carousel_message(
    *,
    db: Session = Depends(deps.get_db),  # noqa: B008
    id: int,
    carousel_message_in: schemas.CarouselMessageUpdate,
    cards_in: list[schemas.CardCreate] | None = None,
    buttons_for_cards_in: list[list[schemas.CardButtonCreate]] | None = None
) -> Any:
    """
    Update a carousel message.
    """
    carousel_message = crud.carousel_message.get(db=db, id=id)
    if not carousel_message:
        raise HTTPException(status_code=404, detail="Carousel message not found")
    carousel_message = crud.carousel_message.update(
        db=db, db_obj=carousel_message, obj_in=carousel_message_in
    )
    if not cards_in:
        return carousel_message
    if not buttons_for_cards_in:
        raise HTTPException(
            status_code=422, detail="You need to provide buttons for the cards"
        )
    for card in carousel_message.cards:
        crud.card.remove(db=db, id=card.id)
    for (card_in, card_buttons_in) in zip(cards_in, buttons_for_cards_in):
        card = crud.card.create_with_message(
            db=db, obj_in=card_in, message_id=carousel_message.id
        )
        for card_button_in in card_buttons_in:
            crud.card_button.create_with_card(
                db=db, obj_in=card_button_in, card_id=card.id
            )
    return carousel_message


@router.get("/{id}", response_model=schemas.CarouselMessage)
def read_carousel_message(
    *, db: Session = Depends(deps.get_db), id: int  # noqa: B008
) -> Any:
    """
    Get carousel message by ID.
    """
    carousel_message = crud.carousel_message.get(db=db, id=id)
    if not carousel_message:
        raise HTTPException(status_code=404, detail="Carousel message not found")
    return carousel_message


@router.delete("/{id}", response_model=schemas.CarouselMessage)
def delete_carousel_message(
    *, db: Session = Depends(deps.get_db), id: int  # noqa: B008
) -> Any:
    """
    Delete a carousel_message
    """
    carousel_message = crud.carousel_message.get(db=db, id=id)
    if not carousel_message:
        raise HTTPException(status_code=404, detail="Carousel message not found")
    carousel_message = crud.carousel_message.remove(db=db, id=id)
    return carousel_message
