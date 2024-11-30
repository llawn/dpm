from app import bcrypt
from pydantic import SecretStr


class AuthMixin:
    @staticmethod
    def generate_password(password: SecretStr) -> SecretStr:
        """generate_password encrypt the password

        encrypt the password using bcrypt
        hide its value using pydantic SecretStr type

        :param password: password (Secret)
        :type password: SecretStr
        :return: return the utf8 value of thee encrypted password (using bcrypt)
        :rtype: SecretStr
        """
        return SecretStr(bcrypt.generate_password_hash(password.get_secret_value()).decode("utf-8"))

    @staticmethod
    def check_password(pw_hash: SecretStr, pw: SecretStr) -> bool:
        """check_password check password for pydantic SecretStr type

        check password using bcript when type is secret

        :param pw_hash: password to guess (hashed)
        :type pw_hash: SecretStr
        :param pw: candidate password (unhashed)
        :type pw: SecretStr
        :return: True if password match the candidate one else False
        :rtype: bool
        """
        return bcrypt.check_password_hash(pw_hash.get_secret_value(), pw.get_secret_value())
