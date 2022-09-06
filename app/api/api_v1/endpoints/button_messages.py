from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=list[schemas.ButtonMessage])
def read_button_messages(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100  # noqa: B008
) -> Any:
    """
    Retrieve button messages.
    """
    button_messages = crud.button_message.get_multi(db=db, skip=skip, limit=limit)
    return button_messages


@router.post("/", response_model=schemas.ButtonMessage)
def create_button_message(
    *,
    db: Session = Depends(deps.get_db),  # noqa: B008
    button_message_in: schemas.ButtonMessageCreate,
    message_buttons_in: list[schemas.MessageButtonCreate]
) -> Any:
    """
    Create new button message.
    """
    button_message = crud.button_message.create(db=db, obj_in=button_message_in)
    for message_button in message_buttons_in:
        crud.message_button.create_with_message(
            db=db, obj_in=message_button, message_id=button_message.id
        )
    return button_message


@router.put("/{id}", response_model=schemas.ButtonMessage)
def update_button_message(
    *,
    db: Session = Depends(deps.get_db),  # noqa: B008
    id: int,
    button_message_in: schemas.ButtonMessageUpdate,
    message_buttons_in: list[schemas.MessageButtonCreate]
) -> Any:
    """
    Update a button message.
    """
    button_message = crud.button_message.get(db=db, id=id)
    if not button_message:
        raise HTTPException(status_code=404, detail="Button message not found")
    button_message = crud.button_message.update(
        db=db, db_obj=button_message, obj_in=button_message_in
    )
    for message_button_in in message_buttons_in:
        crud.message_button.create_with_message(
            db=db, obj_in=message_button_in, message_id=button_message.id
        )
    return button_message


@router.get("/{id}", response_model=schemas.ButtonMessage)
def read_button_message(
    *, db: Session = Depends(deps.get_db), id: int  # noqa: B008
) -> Any:
    """
    Get button message by ID.
    """
    button_message = crud.button_message.get(db=db, id=id)
    if not button_message:
        raise HTTPException(status_code=404, detail="Button message not found")
    return button_message


@router.delete("/{id}", response_model=schemas.ButtonMessage)
def delete_button_message(
    *, db: Session = Depends(deps.get_db), id: int  # noqa: B008
) -> Any:
    """
    Delete a button_message
    """
    button_message = crud.button_message.get(db=db, id=id)
    if not button_message:
        raise HTTPException(status_code=404, detail="Button message not found")
    button_message = crud.button_message.remove(db=db, id=id)
    return button_message
