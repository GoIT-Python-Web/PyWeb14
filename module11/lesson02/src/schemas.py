from pydantic import BaseModel, EmailStr, Field


class OwnerModel(BaseModel):
    email: EmailStr


class ResponseOwner(BaseModel):
    id: int = 1
    email: EmailStr

    class Config:
        orm_mode = True


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
