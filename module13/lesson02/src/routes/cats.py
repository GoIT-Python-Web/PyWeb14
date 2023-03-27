from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Path, Query
from fastapi_limiter.depends import RateLimiter
from sqlalchemy.orm import Session

from src.database.connect import get_db
from src.database.models import User
from src.schemas import ResponsePet, PetModel, PetStatusVaccinated
from src.repository import cats as repository_cats
from src.services.auth import auth_service

router = APIRouter(prefix='/cats', tags=['cats'])


@router.get("/", response_model=List[ResponsePet], dependencies=[Depends(RateLimiter(times=2, seconds=5))])
async def get_cats(limit: int = Query(10, le=1000), offset: int = 0, owner_id: int = None, is_vaccinated: bool = None,
                   db: Session = Depends(get_db), current_user: User = Depends(auth_service.get_current_user)):
    cats = await repository_cats.get_cats(limit, offset, owner_id, is_vaccinated, db)
    return cats


@router.get("/{cat_id}", response_model=ResponsePet)
async def get_cat(cat_id: int = Path(1, ge=1), db: Session = Depends(get_db),
                  current_user: User = Depends(auth_service.get_current_user)):
    cat = await repository_cats.get_cat(cat_id, db)
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return cat


@router.post("/", response_model=ResponsePet, status_code=status.HTTP_201_CREATED)
async def create_cat(body: PetModel, db: Session = Depends(get_db),
                     current_user: User = Depends(auth_service.get_current_user)):
    cat = await repository_cats.create_cat(body, db)
    return cat


@router.put("/{cat_id}", response_model=ResponsePet)
async def update_cat(body: PetModel, cat_id: int = Path(1, ge=1), db: Session = Depends(get_db),
                     current_user: User = Depends(auth_service.get_current_user)):
    cat = await repository_cats.update_cat(body, cat_id, db)
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return cat


@router.patch("/{cat_id}", response_model=ResponsePet)
async def update_cat(body: PetStatusVaccinated, cat_id: int = Path(1, ge=1), db: Session = Depends(get_db),
                     current_user: User = Depends(auth_service.get_current_user)):
    cat = await repository_cats.update_vaccinated_cat(body, cat_id, db)
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return cat


@router.delete("/{cat_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_cat(cat_id: int = Path(1, ge=1), db: Session = Depends(get_db),
                     current_user: User = Depends(auth_service.get_current_user)):
    cat = await repository_cats.remove_cat(cat_id, db)
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return cat
