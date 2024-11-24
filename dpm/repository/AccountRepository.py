from env import db_conn
from models.Account import account_from_data, accounts_from_data


def get_all_accounts():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("""--sql
        SELECT * FROM accounts
    """)
    accounts_data = cur.fetchall()
    cur.close()
    conn.close()
    accounts = accounts_from_data(accounts_data)
    return accounts


def get_account_by_id(user_id):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        """--sql
        SELECT * FROM accounts WHERE user_id = %s
    """,
        (user_id,),
    )
    account_data = cur.fetchone()
    cur.close()
    conn.close()
    account = account_from_data(account_data)
    return account


def get_account_by_username(username):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        """--sql
        SELECT * FROM accounts WHERE username = %s
    """,
        (username,),
    )
    account_data = cur.fetchone()
    cur.close()
    conn.close()
    account = account_from_data(account_data)
    return account


def create_account(username, password, email):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        """--sql
        INSERT INTO accounts
        (username, password, email) VALUES (%s, %s, %s)
        RETURNING user_id;
        """,
        (username, password, email),
    )
    new_account_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_account_id


def update_account(user_id, username, password, email):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        """--sql
        UPDATE accounts
        SET username=%s, password=%s, email=%s
        WHERE user_id = %s
        """,
        (username, password, email, user_id),
    )
    conn.commit()
    cur.close()
    conn.close()


def delete_account(user_id):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        """--sql
        DELETE FROM accounts WHERE user_id = %s
        """,
        (user_id,),
    )
    conn.commit()
    cur.close()
    conn.close()
