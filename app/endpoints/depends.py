
from app.db.base import database
from app.repositories.products import ProductRepository
def get_product_repository() -> ProductRepository:
    return ProductRepository(database)