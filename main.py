from fastapi import FastAPI
from db.base import database
import uvicorn
from endpoints import products
from gi
app = FastAPI(title = "Shop")
app.include_router(products.router, prefix="/product", tags = ["products"])
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
@app.on_event("startup")
async def startup():
    await database.connect()
if __name__ == "__main__":
    uvicorn.run("main:app",port =8000, host = "0.0.0.0", reload=True)
