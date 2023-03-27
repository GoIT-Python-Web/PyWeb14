from sqlalchemy.orm import Session

from src.database.models import Owner
from src.schemas import OwnerModel


async def get_owners(db: Session):
    owners = db.query(Owner).all()
    return owners


async def get_owner(owner_id: int, db: Session):
    owner = db.query(Owner).filter_by(id=owner_id).first()
    return owner


async def create_owner(body: OwnerModel, db: Session):
    owner = Owner(**body.dict())
    db.add(owner)
    db.commit()
    db.refresh(owner)
    return owner


async def update_owner(body: OwnerModel, owner_id: int, db: Session):
    owner = db.query(Owner).filter_by(id=owner_id).first()
    if owner:
        owner.email = body.email
        db.commit()
    return owner


async def remove_owner(owner_id: int, db: Session):
    owner = db.query(Owner).filter_by(id=owner_id).first()
    if owner:
        db.delete(owner)
        db.commit()
    return owner
