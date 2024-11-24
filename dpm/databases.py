from env import db_conn


def init_db():
    conn = db_conn()
    cur = conn.cursor()

    cur.execute("""--sql
        CREATE TABLE IF NOT EXISTS accounts (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(100) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        last_login TIMESTAMP
    );
    """)

    cur.execute("""--sql
        INSERT INTO accounts (username, password, email) VALUES
            ('llawn', 'password', 'llawn06@gmail.com')
        ON CONFLICT (username) DO NOTHING;
    """)

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    init_db()
