from starlette.config import Config
config = Config(".env")
DATABASE_URL = "postgresql://root:root@localhost:32700/shop"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("EE_SECRET_KEY", cast=str, default="e07626a6a7fa220e14363c983b3796453d4f4005034a024f709c1928ce533b57")
