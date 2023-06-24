from typing import List
from app.models.product import Product, ProductIn
from app.repositories.products import ProductRepository
from fastapi import APIRouter, Depends, HTTPException, status, Request
from .depends import get_product_repository
from app.templates_jinja import templates
router = APIRouter()
#GET product
@router.get("/", response_model=List[Product])
async def read_products(request: Request, products: ProductRepository = Depends(get_product_repository),
                        limit: int = 100,
                        skip: int = 0,):
    products_list = await products.get_all(limit=limit, skip=skip)
    rec_list = []
    for rec in products_list:
        rec_list.append(dict(rec))
    response_list = {"request": request, 'products': rec_list}
    return templates.TemplateResponse('index.html', response_list)
#POST product
@router.post("/", response_model=Product)
async def create_job(
    p: ProductIn,
    products: ProductRepository = Depends(get_product_repository)):
    return await products.create(p =  p)