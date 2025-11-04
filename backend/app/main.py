from fastapi import FastAPI
from .database import engine, Base
from app.routes import users, auth, transaction
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

app = FastAPI(
    title="FinManage Backend",
    description="Finance management API",
)

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(transaction.router)

@app.get("/")
def root():
    return {"message": "FinManage backend up"}


