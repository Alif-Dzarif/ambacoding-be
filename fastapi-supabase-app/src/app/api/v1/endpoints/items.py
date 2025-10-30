from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.crud.user import get_user, create_user
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_item(item: UserCreate, db: Session = Depends(get_db)):
    db_item = get_user(db, item.username)
    if db_item:
        raise HTTPException(status_code=400, detail="Item already registered")
    return create_user(db=db, user=item)

@router.get("/{item_id}", response_model=UserResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = get_user(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/{item_id}", response_model=UserResponse)
def update_item(item_id: int, item: UserCreate, db: Session = Depends(get_db)):
    db_item = get_user(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return create_user(db=db, user=item)

@router.delete("/{item_id}", response_model=UserResponse)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = get_user(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    # Logic to delete the item goes here
    return {"detail": "Item deleted successfully"}