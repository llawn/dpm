from datetime import UTC, datetime
from typing import Self

from customtypes import UsernameStr
from pydantic import BaseModel, EmailStr, PositiveInt, SecretStr


class User(BaseModel):
    user_id: PositiveInt
    username: UsernameStr
    password: SecretStr
    email: EmailStr
    created_at: str = datetime.now(UTC).replace(tzinfo=None).isoformat()
    last_login: str | None = None

    @staticmethod
    def get_iso(dt: datetime) -> str:
        return dt.astimezone(UTC).replace(tzinfo=None).isoformat()

    @classmethod
    def from_datetime(
        cls,
        user_id: PositiveInt,
        username: UsernameStr,
        password: SecretStr,
        email: EmailStr,
        created_at: datetime | None = None,
        last_login: datetime | None = None,
    ) -> Self:
        created_at_iso = cls.get_iso(created_at) if created_at else None
        last_login_iso = cls.get_iso(created_at) if last_login else None
        return cls(
            user_id=user_id,
            username=username,
            password=password,
            email=email,
            created_at=created_at_iso,
            last_login=last_login_iso,
        )
