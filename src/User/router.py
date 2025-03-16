from typing import Annotated
from fastapi import APIRouter, Query, HTTPException

from src.core.db import SessionDep
from .model import User
from sqlmodel import select

router = APIRouter(tags=["users"])




@router.post("/users/")
def create_user(user: User, session: SessionDep) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.get("/users/" )
async def read_users(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
) -> list[User]:
    Users = session.exec(select(User).offset(offset).limit(limit)).all()
    return Users


@router.get("/users/{user_id}")
def read_user(user_id: int, session: SessionDep) -> User:
    user = session.get(User,user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/users/{user_id}")
def delete_user(user_id: int, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"ok": True}

# @router.get("/users/me")
# async def read_user_me():
#     return {"username": "fakecurrentuser"}
#
#
# @router.get("/users/{username}")
# async def read_user(username: str):
#     return {"username": username}


