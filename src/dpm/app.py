from dynaconf import FlaskDynaconf
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

flask_dynaconf = FlaskDynaconf(app, settings_files=["settings.toml", ".secrets.toml"])
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
def home():
    return {
        "app_name": app.config.get("APP_NAME"),
        "debug": app.config.get("DEBUG"),
        "port": app.config.get("PORT"),
        "host": app.config.get("HOST"),
        "user": app.config.get("USER"),
    }


def start():
    """start the app

    initialize database and run app
    """
    from databases import DatabaseConnMixin

    DatabaseConnMixin.create_db()
    DatabaseConnMixin.init_db_entry()
    app.run(port=5000, debug=True)


if __name__ == "__main__":
    start()
