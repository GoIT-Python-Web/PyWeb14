from datetime import datetime

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


class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=16)
    email: str
    password: str = Field(min_length=6, max_length=10)


class UserDb(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    avatar: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    