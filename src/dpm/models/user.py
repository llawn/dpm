from datetime import datetime

from customtypes import UsernameStr
from pydantic import AwareDatetime, BaseModel, EmailStr, PositiveInt, SecretStr


class User(BaseModel):
    user_id: PositiveInt
    username: UsernameStr
    password: SecretStr
    email: EmailStr
    created_at: AwareDatetime = datetime.now(tz=datetime.now().astimezone().tzinfo)
    last_login: AwareDatetime | None = None

    @classmethod
    def from_iso(
        cls,
        user_id: PositiveInt,
        username: UsernameStr,
        password: SecretStr,
        email: EmailStr,
        created_at_iso: str,
        last_login_iso: str | None = None,
    ):
        created_at = datetime.fromisoformat(created_at_iso)
        last_login = datetime.fromisoformat(last_login_iso) if last_login_iso else None
        return cls(
            user_id=user_id,
            username=username,
            password=password,
            email=email,
            created_at=created_at,
            last_login=last_login,
        )
