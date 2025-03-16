from fastapi import FastAPI, Depends

from src.dependencies import get_token_header, get_query_token
from User.router import router as user_router
from item.items import router as item_router

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(user_router)
app.include_router(item_router)



@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}



# @app.get("/item")
# async def get_item():
#     return {"item": "hello"}

