from fastapi import FastAPI
from app.db.base import database
import uvicorn
from app.endpoints import products, users
from starlette.staticfiles import StaticFiles

app = FastAPI(title = "Shop")
#app.mount(path="/static",app = StaticFiles(directory="todo/staticcss"), name = "static")
app.include_router(products.router, prefix="/product", tags = ["products"])
app.include_router(users.router, prefix = "/user", tags=["users"])
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
@app.on_event("startup")
async def startup():
    await database.connect()
if __name__ == "__main__":
    uvicorn.run("main:app",port =8000, host = "0.0.0.0", reload=True)
