from datetime import datetime

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    user_id: int
    username: str
    password: str
    email: EmailStr
    created_at: datetime
    last_login: datetime


user = User(
    user_id=1,
    username="johndoe",
    password="securepassword123",
    email="johndoe@example.com",
    created_at=datetime.now(),
    last_login=datetime.now(),
)

print(user.model_dump())
