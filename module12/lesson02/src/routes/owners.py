from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session

from src.database.connect import get_db
from src.schemas import ResponseOwner, OwnerModel
from src.repository import owners as repository_owners

router = APIRouter(prefix='/owners', tags=['owners'])


@router.get("/", response_model=List[ResponseOwner], )
async def get_owners(db: Session = Depends(get_db)):
    owners = await repository_owners.get_owners(db)
    return owners


@router.get("/{owner_id}", response_model=ResponseOwner)
async def get_owner(owner_id: int = Path(1, ge=1), db: Session = Depends(get_db)):
    owner = await repository_owners.get_owner(owner_id, db)
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return owner


@router.post("/", response_model=ResponseOwner, status_code=status.HTTP_201_CREATED)
async def create_owner(body: OwnerModel, db: Session = Depends(get_db)):
    owner = await repository_owners.create_owner(body, db)
    return owner


@router.put("/{owner_id}", response_model=ResponseOwner)
async def update_owner(body: OwnerModel, owner_id: int = Path(1, ge=1), db: Session = Depends(get_db)):
    owner = await repository_owners.update_owner(body, owner_id, db)
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return owner


@router.delete("/{owner_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_owner(owner_id: int = Path(1, ge=1), db: Session = Depends(get_db)):
    owner = await repository_owners.remove_owner(owner_id, db)
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return owner
