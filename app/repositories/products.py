from typing import List, Optional
import datetime
from app.models.product import Product, ProductIn
from app.db.products import products
from .base import BaseRepository

class ProductRepository(BaseRepository):
    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Product]:
        query = products.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)
    async def create(self, p: ProductIn) -> Product:
        product = Product(
            id=p.id,
            name=p.name,
            category=p.category,
            original_price=p.original_price,
            product_img=p.product_img,
            created_at = datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow()
        )
        values = {**product.dict()}
        values.pop("id", None)
        query = products.insert().values(**values)
        product.id = await self.database.execute(query=query)
        return product