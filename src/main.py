from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_items():
    return {"items": "hello"}

@app.get("/item")
async def get_item():
    return {"item": "hello"}

