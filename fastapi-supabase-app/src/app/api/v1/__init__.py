# File: /fastapi-supabase-app/fastapi-supabase-app/src/app/api/v1/__init__.py

from fastapi import APIRouter

router = APIRouter()

from .endpoints import auth, users, items

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(items.router, prefix="/items", tags=["items"])