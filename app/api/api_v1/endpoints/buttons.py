from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=list[schemas.Button])
def get_buttons(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 0  # noqa: B008
) -> Any:
    """
    Retrieve buttons.
    """
    buttons = crud.button.get_multi(db, skip=skip, limit=limit)
    return buttons


@router.get("/{id}", response_model=schemas.Button)
def get_button(*, db: Session = Depends(deps.get_db), id: int) -> Any:  # noqa: B008
    """
    Get button by ID.
    """
    button = crud.button.get(db=db, id=id)
    if not button:
        raise HTTPException(status_code=404, detail="button not found")
    return button


@router.delete("/{id}", response_model=schemas.Button)
def delete_button(*, db: Session = Depends(deps.get_db), id: int) -> Any:  # noqa: B008
    """
    Delete button.
    """
    button = crud.button.get(db=db, id=id)
    if not button:
        raise HTTPException(status_code=404, detail="button not found")
    button = crud.button.remove(db=db, id=id)
    return button
