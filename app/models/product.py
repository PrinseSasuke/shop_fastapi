from typing import Optional
from pydantic import BaseModel, EmailStr, validator, constr
import datetime
class Product(BaseModel):
    id:int
    name:str
    category:str
    original_price:int
    product_img:str
    created_at: datetime.datetime
    updated_at:datetime.datetime
class ProductIn(BaseModel):
    id:int
    name:str
    category:str
    original_price:int
    product_img:str