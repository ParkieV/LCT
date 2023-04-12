from fastapi import UploadFile
from pydantic import BaseModel, EmailStr


class RegisterUserRequest(BaseModel):
    name: str
    email: str


class RegisterUser(RegisterUserRequest):
    id: int

    class Config:
        orm_mode = True


class LoginUserRequest(BaseModel):
    email: str
    password: str


class User(BaseModel):
    id: int
    name: str
    email: str
    role: str
    hashed_password: str
    work_counter: int
    is_banned: bool

    class Config:
        orm_mode = True


class LoginUserOut(BaseModel):
    user: User
    password: str


class RegisterUserRequest(BaseModel):
    name: str
    email: str


class Flat(BaseModel):
    address: str
    num_rooms: int
    building_segment: str
    building_num_floors: int
    building_material: str
    floor: int
    square_flat: float
    square_kitchen: float
    has_balcony: bool
    metro_distance: int
    condition: str


class FlatRequest(BaseModel):
    flats_prices: list[float]
    filename: str


class UploadFileRequest(BaseModel):
    file: UploadFile
    user: User


class CalculateCostRequest(BaseModel):
    flats: list[Flat]
    base_flats: dict[int, Flat]


class DownloadFileRequest(BaseModel):
    flats_prices: list[float]
    filename: str


class EmailSchema(BaseModel):
    email: EmailStr

