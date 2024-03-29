from typing import Optional
from pydantic import BaseModel, EmailStr, validator, constr
import datetime
class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: EmailStr
    hashed_password: str
    is_admin: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime

class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length = 8)
    password2: constr(min_length = 8)
    is_admin: bool = False
    @validator("password2")
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values["password"]:
            raise ValueError("passwords don't match")
        return v