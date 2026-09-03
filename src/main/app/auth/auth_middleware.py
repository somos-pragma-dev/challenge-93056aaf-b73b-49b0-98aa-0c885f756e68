from fastapi import Request, HTTPException, Depends
from.security_config import get_current_user

async def auth_middleware(request: Request):
    user_id = await get_current_user(token=request.headers.get("Authorization"))
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return user_id