from fastapi import FastAPI, Depends

from src.dependencies import get_token_header, get_query_token
from src.User import router as user
from src.item import items
from src.internal import admin

from src.core.db import create_db_and_tables


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(user.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)





@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}



# @app.get("/item")
# async def get_item():
#     return {"item": "hello"}

