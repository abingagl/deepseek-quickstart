from fastapi import Header, HTTPException
from data_store import USERS

async def get_current_user(x_user_id: str = Header(...)):
    if x_user_id not in USERS:
        raise HTTPException(status_code=401, detail="Invalid user")
    return USERS[x_user_id]