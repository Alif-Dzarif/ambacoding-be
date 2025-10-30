from sqlalchemy.orm import Session
from app.models.user import User
from app.db.session import get_db

def seed_users(db: Session):
    users = [
        User(username="user1", email="user1@example.com", password="hashed_password1"),
        User(username="user2", email="user2@example.com", password="hashed_password2"),
        User(username="user3", email="user3@example.com", password="hashed_password3"),
    ]
    
    db.add_all(users)
    db.commit()
    db.refresh(users)
    return users

if __name__ == "__main__":
    db = next(get_db())
    seed_users(db)