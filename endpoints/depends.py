
from db.base import database
from repositories.products import ProductRepository
def get_product_repository() -> ProductRepository:
    return ProductRepository(database)