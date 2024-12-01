import psycopg2
from pydantic import SecretStr

from .app import app
from .auth import AuthMixin
from .models.settings import DatabaseConnSettings


class DatabaseConnMixin:
    @staticmethod
    def load_conn_setttings() -> DatabaseConnSettings:
        """load_conn_setttings load settings and validation with pydantic

        get configuration with dynaconf, load settings with pydantic

        :return: Database Connection Settings model
        :rtype: DatabaseConnSettings
        """
        data = {
            "database": app.config.get("DATABASE"),
            "host": app.config.get("HOST"),
            "user": app.config.get("USER"),
            "password": SecretStr(app.config.get("PASSWORD")),
            "port": app.config.get("PORT"),
        }
        conn_settings = DatabaseConnSettings(**data)  # Validation
        return conn_settings

    def db_conn(self) -> psycopg2.extensions.connection:
        """db_conn connect to the database

        connect to the database based on the dynaconf settings

        :return: psycopg2 connection object
        :rtype: psycopg2.extensions.connection
        """
        conn_settings = self.load_conn_setttings()
        conn = psycopg2.connect(**conn_settings.model_dump_secret())
        return conn

    def create_db(self) -> None:
        """create_db create database structure

        create the different tables
        """
        conn = self.db_conn()
        cur = conn.cursor()

        cur.execute("""--sql
            SET timezone = 'UTC';
            CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            last_login TIMESTAMP
        );
        """)
        cur.close()
        conn.close()

    def init_db_entry(self) -> None:
        """init_db_entry initialize tables with an entry

        add an entry to not have empty table (use for testing)
        """

        conn = self.db_conn()
        cur = conn.cursor()
        pw = AuthMixin.generate_password(SecretStr("password")).get_secret_value()

        cur.execute(
            """--sql
            INSERT INTO users (username, password, email) VALUES
                (%s, %s, %s)
            ON CONFLICT (username) DO NOTHING;
        """,
            ("testuser", pw, "testuser@example.com"),
        )
        conn.commit()
        cur.close()
        conn.close()
