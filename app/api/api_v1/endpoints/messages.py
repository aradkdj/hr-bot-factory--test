from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=list[schemas.Message])
def get_messages(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 0  # noqa: B008
) -> Any:
    """
    Retrieve messages.
    """
    messages = crud.message.get_multi(db, skip=skip, limit=limit)
    return messages


@router.get("/{id}", response_model=schemas.Message)
def get_message(*, db: Session = Depends(deps.get_db), id: int) -> Any:  # noqa: B008
    """
    Get message by ID.
    """
    message = crud.message.get(db=db, id=id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message


@router.delete("/{id}", response_model=schemas.Message)
def delete_message(*, db: Session = Depends(deps.get_db), id: int) -> Any:  # noqa: B008
    """
    Delete message.
    """
    message = crud.message.get(db=db, id=id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    message = crud.message.remove(db=db, id=id)
    return message
