from sqlalchemy.orm import Session

from src.database.models import Cat
from src.schemas import PetModel, PetStatusVaccinated


async def get_cats(limit: int, offset: int, owner_id: int, is_vaccinated: bool, db: Session):
    owners = db.query(Cat)
    if owner_id:
        owners = owners.filter(Cat.owner_id == owner_id)
    print(is_vaccinated)
    if is_vaccinated is not None:
        owners = owners.filter(Cat.vaccinated == is_vaccinated)
    owners = owners.limit(limit).offset(offset).all()
    return owners


async def get_cat(cat_id: int, db: Session):
    owner = db.query(Cat).filter_by(id=cat_id).first()
    return owner


async def create_cat(body: PetModel, db: Session):
    cat = Cat(**body.dict())
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat


async def update_cat(body: PetModel, cat_id: int, db: Session):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat:
        cat.nickname = body.nickname
        cat.age = body.age
        cat.vaccinated = body.vaccinated
        cat.description = body.description
        cat.owner_id = body.owner_id
        db.commit()
    return cat


async def update_vaccinated_cat(body: PetStatusVaccinated, cat_id: int, db: Session):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat:
        cat.vaccinated = body.vaccinated
        db.commit()
    return cat


async def remove_cat(cat_id: int, db: Session):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat:
        db.delete(cat)
        db.commit()
    return cat
