from datetime import UTC, datetime
from typing import Self

from pydantic import BaseModel, EmailStr, PositiveInt, SecretStr

from .customtypes import UsernameStr


class User(BaseModel):
    """User model to represent a user

    use pydantic BaseModel for validation

    :param user_id: user id
    :type user_id: PositiveInt
    :param username: username adhering to `StringConstraints`
    :type username: UsernameStr
    :param password: user password
    :type password: SecretStr
    :param email: user email
    :type email: EmailStr
    :param created_at: datetime of creation in ISO format (UTC), defaults to
        `datetime.now(UTC).replace(tzinfo=None).isoformat()`
    :type created_at: str, optional
    :param last_login: datetime of last connection in ISO format (UTC), defaults to None
    :type last_login: str, optional
    """

    user_id: PositiveInt
    username: UsernameStr
    password: SecretStr
    email: EmailStr
    created_at: str = datetime.now(UTC).replace(tzinfo=None).isoformat()
    last_login: str | None = None

    @staticmethod
    def get_iso(dt: datetime) -> str:
        """get_iso convert datetime to ISO string format

        The datetime is convert at UTC and timezone is erased

        :param dt: datetime to convert
        :type dt: datetime
        :return: ISO format of dt
        :rtype: str
        """
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
        """from_datetime create user from datetime

        create_at and last_login are converted to ISO format using `get_iso`

        :param user_id: user id
        :type user_id: PositiveInt
        :param username: username adhering to `StringConstraints`
        :type username: UsernameStr
        :param password: user password
        :type password: SecretStr
        :param email: user email
        :type email: EmailStr
        :param created_at: datetime of creation, defaults to None
        :type created_at: datetime, optional
        :param last_login: datetime of last login, defaults to None
        :type last_login: datetime, optional
        :return: user
        :rtype: User
        """
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
