from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session

from src.database.connect import get_db
from src.database.models import User, Roles
from src.schemas import ResponseOwner, OwnerModel
from src.repository import owners as repository_owners
from src.services.auth import auth_service
from src.services.roles import RoleChecker

router = APIRouter(prefix='/owners', tags=['owners'])

allowed_get_owners = RoleChecker([Roles.admin, Roles.moderator, Roles.user])
allowed_create_owners = RoleChecker([Roles.admin, Roles.moderator, Roles.user])
allowed_update_owners = RoleChecker([Roles.admin, Roles.moderator])
allowed_remove_owners = RoleChecker([Roles.admin])


@router.get("/", response_model=List[ResponseOwner], dependencies=[Depends(allowed_get_owners)])
async def get_owners(db: Session = Depends(get_db), current_user: User = Depends(auth_service.get_current_user)):
    owners = await repository_owners.get_owners(db)
    return owners


@router.get("/{owner_id}", response_model=ResponseOwner, dependencies=[Depends(allowed_get_owners)])
async def get_owner(owner_id: int = Path(1, ge=1), db: Session = Depends(get_db),
                    current_user: User = Depends(auth_service.get_current_user)):
    owner = await repository_owners.get_owner(owner_id, db)
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return owner


@router.post("/", response_model=ResponseOwner, status_code=status.HTTP_201_CREATED,
             dependencies=[Depends(allowed_create_owners)])
async def create_owner(body: OwnerModel, db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)):
    owner = await repository_owners.create_owner(body, db)
    return owner


@router.put("/{owner_id}", response_model=ResponseOwner, dependencies=[Depends(allowed_update_owners)])
async def update_owner(body: OwnerModel, owner_id: int = Path(1, ge=1), db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)):
    owner = await repository_owners.update_owner(body, owner_id, db)
    # owner.user_id != current_user.id
    # raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Operation forbidden")
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return owner


@router.delete("/{owner_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(allowed_remove_owners)])
async def remove_owner(owner_id: int = Path(1, ge=1), db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)):
    owner = await repository_owners.remove_owner(owner_id, db)
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return owner
