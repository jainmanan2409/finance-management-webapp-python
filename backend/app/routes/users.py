from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, utils, oauth2
from app.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# ---------- CREATE USER ----------
@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Hash the password before saving
    hashed_password = utils.hash_password(user.password)
    new_user = models.User(name=user.name, email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# ---------- GET ALL USERS ----------
@router.get("/", response_model=list[schemas.UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

# ---------- GET USER LOGGED IN----------
@router.get("/me")
def get_current_user(
    current_user: models.User = Depends(oauth2.get_current_user)
):
    return current_user

# ---------- GET USER BY ID ----------
@router.get("/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
