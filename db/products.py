import sqlalchemy
from .base import metadata
import datetime
products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("category", sqlalchemy.String),
    sqlalchemy.Column("original_price", sqlalchemy.Integer),
    sqlalchemy.Column("product_img", sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, default = datetime.datetime.utcnow())
    )