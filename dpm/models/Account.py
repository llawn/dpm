from flask_login import UserMixin


class Account(UserMixin):
    def __init__(self, user_id, username, password, email, created_at, last_login):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.created_at = created_at
        self.last_login = last_login

    def get_id(self):
        """Override get_id method from UserMixin"""
        return str(self.user_id)

    def to_dict(self):
        dict = {
            "user_id": self.user_id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "created_at": self.created_at,
            "last_login": self.last_login,
        }
        return dict

    def check_password(self, password):
        # TODO hash_password
        return self.password == password.decode("utf-8")


def account_from_data(account_data):
    # TODO: no number only string
    if account_data:
        account = Account(
            user_id=account_data[0],
            username=account_data[1],
            password=account_data[2],
            email=account_data[3],
            created_at=account_data[4],
            last_login=account_data[5],
        )
        return account


def accounts_from_data(accounts_data):
    accounts = [account_from_data(account_data) for account_data in accounts_data]
    return accounts
