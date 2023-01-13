import json
from pprint import pprint
from typing import Any, List, Union

from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Item])
def read_items(
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve items.
    """
    items = crud.item.get_multi(db, )

    return items


# @router.post("/", response_model=schemas.Item)
@router.post("/", )
def create_item(
        *,
        db: Session = Depends(deps.get_db),

        item_in: Union[schemas.ItemCreate, bytes],
) -> Any:
    """
    Create new item.
    """
    if isinstance(item_in, bytes):
        item_in = schemas.ItemCreate(**json.loads(item_in))

    # print("In POST endpoint. This is what I got")  # b'{"title":"asdsad","checked":false}' from FE
    # pprint(item_in)
    #
    # print(isinstance(item_in, bytes))

    item = crud.item.create(db=db, obj_in=item_in)
    return item


@router.put("/{id}", response_model=schemas.Item)
def update_item(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        item_in: Union[schemas.ItemUpdate, bytes],
) -> Any:
    """
    Update an item.
    """
    if isinstance(item_in, bytes):
        item_in = schemas.ItemUpdate(**json.loads(item_in))

    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item = crud.item.update(db=db, db_obj=item, obj_in=item_in)
    return item


@router.delete("/{id}", response_model=schemas.Item)
def delete_item(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
) -> Any:
    """
    Delete an item.
    """
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item = crud.item.remove(db=db, id=id)
    return item
