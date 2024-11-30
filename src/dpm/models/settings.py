from pydantic import BaseModel, PositiveInt, SecretStr

from .customtypes import UsernameStr


class DatabaseConnSettings(BaseModel):
    """Connection settings to a database

    :param database: database
    :type databse: databse
    :param host: host
    :type host: str
    :param password: password
    :type password: SecretStr
    :param port: port
    :type port: PositiveInt
    :param user: user
    :type user: UsernameStr
    """

    database: str
    host: str
    password: SecretStr
    port: PositiveInt
    user: UsernameStr

    def model_dump_secret(self) -> dict:
        """model_dump_secret pydantic model_dump with secret value

        give the secret value of the settings to help integration with other function

        :return: model_dump without SecretStr
        :rtype: dict
        """
        data = self.model_dump()
        data["password"] = self.password.get_secret_value()
        return data
