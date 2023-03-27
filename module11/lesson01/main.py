import time
from typing import List

from fastapi import FastAPI, Depends, HTTPException, status, Path, Query, Request
from sqlalchemy import text
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr, Field

from connect_db import get_db
from models import Owner, Cat

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["My-Process-Time"] = str(process_time)
    response.headers.update({"server": "GoIt web 8 group"})
    # response.headers["server"] = "Django"
    return response


@app.get("/", name='Корінь проекту')
def read_root():
    return {"message": "REST APP v1.0"}


@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)):
    try:
        # Make request
        result = db.execute(text("SELECT 1")).fetchone()
        print(result)
        if result is None:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Error connecting to the database")


class OwnerModel(BaseModel):
    email: EmailStr


class ResponseOwner(BaseModel):
    id: int = 1
    email: EmailStr

    class Config:
        orm_mode = True


@app.get("/owners", response_model=List[ResponseOwner], tags=['owners'])
async def get_owners(db: Session = Depends(get_db)):
    owners = db.query(Owner).all()
    return owners


@app.get("/owners/{owner_id}", response_model=ResponseOwner, tags=['owners'])
async def get_owner(owner_id: int = Path(1, ge=1), db: Session = Depends(get_db)):
    owner = db.query(Owner).filter_by(id=owner_id).first()
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return owner


@app.post("/owners", response_model=ResponseOwner, tags=['owners'])
async def create_owner(body: OwnerModel, db: Session = Depends(get_db)):
    owner = Owner(**body.dict())
    db.add(owner)
    db.commit()
    db.refresh(owner)
    return owner


@app.put("/owners/{owner_id}", response_model=ResponseOwner, tags=['owners'])
async def update_owner(body: OwnerModel, owner_id: int = Path(1, ge=1), db: Session = Depends(get_db)):
    owner = db.query(Owner).filter_by(id=owner_id).first()
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    owner.email = body.email
    db.commit()
    return owner


@app.delete("/owners/{owner_id}", status_code=status.HTTP_204_NO_CONTENT, tags=['owners'])
async def remove_owner(owner_id: int = Path(1, ge=1), db: Session = Depends(get_db)):
    owner = db.query(Owner).filter_by(id=owner_id).first()
    if owner is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    db.delete(owner)
    db.commit()
    return owner


class PetModel(BaseModel):
    nickname: str = Field('Barsik', min_length=3, max_length=12)
    age: int = Field(1, ge=0, le=30)
    vaccinated: bool = False
    description: str
    owner_id: int = Field(1, gt=0)


class PetStatusVaccinated(BaseModel):
    vaccinated: bool


class ResponsePet(BaseModel):
    id: int = 1
    nickname: str
    age: int
    vaccinated: bool
    description: str
    owner: ResponseOwner

    class Config:
        orm_mode = True


@app.get("/cats", response_model=List[ResponsePet], tags=['cats'])
async def get_cats(limit: int = Query(10, le=1000), offset: int = 0, db: Session = Depends(get_db)):
    cats = db.query(Cat).limit(limit).offset(offset).all()
    return cats


@app.get("/cats/{cat_id}", response_model=ResponsePet, tags=['cats'])
async def get_cat(cat_id: int = Path(1, ge=1), db: Session = Depends(get_db)):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return cat


@app.post("/cats", response_model=ResponsePet, tags=['cats'])
async def create_cat(body: PetModel, db: Session = Depends(get_db)):
    cat = Cat(**body.dict())
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat


@app.put("/cats/{cat_id}", response_model=ResponsePet, tags=['cats'])
async def update_cat(body: PetModel, cat_id: int = Path(1, ge=1), db: Session = Depends(get_db)):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    cat.nickname = body.nickname
    cat.age = body.age
    cat.vaccinated = body.vaccinated
    cat.description = body.description
    cat.owner_id = body.owner_id
    db.commit()
    return cat


@app.patch("/cats/{cat_id}", response_model=ResponsePet, tags=['cats'])
async def update_cat(body: PetStatusVaccinated, cat_id: int = Path(1, ge=1), db: Session = Depends(get_db)):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    cat.vaccinated = body.vaccinated
    db.commit()
    return cat


@app.delete("/cats/{cat_id}", status_code=status.HTTP_204_NO_CONTENT, tags=['cats'])
async def remove_cat(cat_id: int = Path(1, ge=1), db: Session = Depends(get_db)):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    db.delete(cat)
    db.commit()
    return cat
