from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud.user import get_user, update_user
from app.schemas.user import UserUpdate, UserResponse
from app.auth.deps import get_current_user

router = APIRouter()

@router.get("/me", response_model=UserResponse)
async def read_users_me(current_user: UserResponse = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=UserResponse)
async def update_users_me(user_update: UserUpdate, current_user: UserResponse = Depends(get_current_user), db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=current_user.id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = update_user(db=db, user_id=current_user.id, user_update=user_update)
    return updated_user