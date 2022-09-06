from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=list[schemas.Way])
def read_ways(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100  # noqa: B008
) -> Any:
    """
    Retrieve ways.
    """
    ways = crud.way.get_multi(db=db, skip=skip, limit=limit)
    return ways


@router.post("/", response_model=schemas.Way)
def create_way(
    *, db: Session = Depends(deps.get_db), way_in: schemas.WayCreate  # noqa: B008
) -> Any:
    """
    Create new item.
    """
    way = crud.way.create(db=db, obj_in=way_in)
    return way


@router.put("/{id}", response_model=schemas.Way)
def update_way(
    *,
    db: Session = Depends(deps.get_db),  # noqa: B008
    id: int,
    way_in: schemas.WayUpdate
) -> Any:
    """
    Update a way.
    """
    way = crud.way.get(db=db, id=id)
    if not way:
        raise HTTPException(status_code=404, detail="Way not found")
    way = crud.way.update(db=db, db_obj=way, obj_in=way_in)
    return way


@router.get("/{id}", response_model=schemas.Way)
def read_way(*, db: Session = Depends(deps.get_db), id: int) -> Any:  # noqa: B008
    """
    Get way by ID.
    """
    way = crud.way.get(db=db, id=id)
    if not way:
        raise HTTPException(status_code=404, detail="Way not found")
    return way


@router.delete("/{id}", response_model=schemas.Way)
def delete_way(*, db: Session = Depends(deps.get_db), id: int) -> Any:  # noqa: B008
    """
    Delete a way.
    """
    way = crud.way.get(db=db, id=id)
    if not way:
        raise HTTPException(status_code=404, detail="Way not found")
