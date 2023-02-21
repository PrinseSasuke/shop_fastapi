from typing import List
from models.product import Product, ProductIn
from repositories.products import ProductRepository
from fastapi import APIRouter, Depends, HTTPException, status
from .depends import get_product_repository

router = APIRouter()

@router.get("/", response_model=List[Product])
async def read_products(products: ProductRepository = Depends(get_product_repository),
                        limit: int = 100,
                        skip: int = 0,):
    return await products.get_all(limit=limit, skip=skip)

@router.post("/", response_model=Product)
async def create_job(
    p: ProductIn,
    products: ProductRepository = Depends(get_product_repository)):
    return await products.create(p=p)