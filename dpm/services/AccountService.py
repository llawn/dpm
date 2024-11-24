from repository.AccountRepository import (
    create_account,
    delete_account,
    get_account_by_id,
    get_account_by_username,
    get_all_accounts,
    update_account,
)


def get_all_accounts_service():
    return get_all_accounts()


def get_account_by_id_service(id):
    return get_account_by_id(id)


def get_account_by_username_service(username):
    return get_account_by_username(username)


def create_account_service(username, password, email):
    return create_account(username, password, email)


def delete_account_service(user_id):
    delete_account(user_id)


def update_account_service(user_id, username, password, email):
    update_account(user_id, username, password, email)
