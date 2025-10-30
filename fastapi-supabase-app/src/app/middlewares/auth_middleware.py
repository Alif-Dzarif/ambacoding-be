from fastapi import Request, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.auth.deps import get_current_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def auth_middleware(request: Request, call_next):
    if request.url.path.startswith("/api/v1/protected"):
        token = request.headers.get("Authorization")
        if not token:
            raise HTTPException(status_code=401, detail="Not authenticated")
        
        try:
            user = await get_current_user(token)
        except Exception:
            raise HTTPException(status_code=403, detail="Not authorized")
    
    response = await call_next(request)
    return response