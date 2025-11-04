from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import models, utils, oauth2
from app.database import get_db

router = APIRouter(prefix="/login", tags=["Authentication"])

@router.post("/", tags=["Authentication"])
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    

    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user or not utils.verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid Credentials"
        )


    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
