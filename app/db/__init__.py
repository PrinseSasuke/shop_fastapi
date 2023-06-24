
from .products import products
from .users import users
from .base import metadata, engine
metadata.drop_all(bind=engine)
metadata.create_all(bind=engine)