from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from enum import Enum


class TransactionType(str, Enum):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"


# ---------- USER SCHEMAS ----------
class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # allows reading SQLAlchemy models directly


# ---------- TRANSACTION SCHEMAS ----------
class TransactionBase(BaseModel):

    amount: float
    type: TransactionType
    note: str | None = None



class TransactionCreate(TransactionBase):
    pass


class TransactionResponse(TransactionBase):
    id: int
    created_at: datetime


    class Config:
        from_attributes = True
