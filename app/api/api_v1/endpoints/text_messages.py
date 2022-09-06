from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=list[schemas.TextMessage])
def read_text_messages(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100  # noqa: B008
) -> Any:
    """
    Retrieve text messages.
    """
    text_messages = crud.text_message.get_multi(db=db, skip=skip, limit=limit)
    return text_messages


@router.post("/", response_model=schemas.TextMessage)
def create_text_message(
    *,
    db: Session = Depends(deps.get_db),  # noqa: B008
    message_in: schemas.TextMessageCreate
) -> Any:
    """
    Create new text message.
    """
    text_message = crud.text_message.create(db=db, obj_in=message_in)
    return text_message


@router.put("/{id}", response_model=schemas.TextMessage)
def update_text_message(
    *,
    db: Session = Depends(deps.get_db),  # noqa: B008
    id: int,
    text_message_in: schemas.TextMessageUpdate
) -> Any:
    """
    Update a text message.
    """
    text_message = crud.text_message.get(db=db, id=id)
    if not text_message:
        raise HTTPException(status_code=404, detail="Text message not found")
    text_message = crud.text_message.update(
        db=db, db_obj=text_message, obj_in=text_message_in
    )
    return text_message


@router.get("/{id}", response_model=schemas.TextMessage)
def read_text_message(
    *, db: Session = Depends(deps.get_db), id: int  # noqa: B008
) -> Any:
    """
    Get text message by ID.
    """
    text_message = crud.text_message.get(db=db, id=id)
    if not text_message:
        raise HTTPException(status_code=404, detail="Text message not found")
    return text_message


@router.delete("/{id}", response_model=schemas.TextMessage)
def delete_text_message(
    *, db: Session = Depends(deps.get_db), id: int  # noqa: B008
) -> Any:
    """
    Delete a text_message
    """
    text_message = crud.text_message.get(db=db, id=id)
    if not text_message:
        raise HTTPException(status_code=404, detail="Text message not found")
    text_message = crud.text_message.remove(db=db, id=id)
    return text_message
