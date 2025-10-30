from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserOut
from app.auth.service import create_user, authenticate_user
from app.auth.deps import get_current_user

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db=db, user=user)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User already registered")
    return db_user

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    access_token = authenticate_user(db=db, username=user.username, password=user.password)
    if not access_token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me", response_model=UserOut)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user