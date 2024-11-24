from databases import init_db
from env import get_secret_key
from flask import Flask, redirect, render_template, request, url_for
from flask_limiter import Limiter
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_wtf import FlaskForm
from routes.AccountRoutes import accounts_bp
from services.AccountService import get_account_by_id_service, get_account_by_username_service
from wtforms import PasswordField, StringField
from wtforms.validators import InputRequired, Length

## SECURE FORM FOR AUTH


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=4)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8)])


## APP

app = Flask(__name__)
app.secret_key = get_secret_key()  # For session management

app.config.update(
    SESSION_COOKIE_SECURE=True,  # Only sent over HTTPS
    SESSION_COOKIE_HTTPONLY=True,  # JavaScript cannot access the session cookie
    SESSION_COOKIE_SAMESITE="Strict",  # Prevent CSRF attacks
)

app.register_blueprint(accounts_bp)

## LOGIN MANAGER

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    account = get_account_by_id_service(user_id)
    return account


## LOGIN ROUTE

limiter = Limiter(app)


@app.route("/login", methods=["GET", "POST"])
@limiter.limit("5/minute")  # Allow only 5 requests per minute
def login():
    if request.method == "POST":
        # Get the data from the form
        username = request.form["username"]
        password = request.form["password"].encode("utf-8")
        existing_account = get_account_by_username_service(username)
        if existing_account:
            if existing_account.check_password(password):
                login_user(existing_account)
                return redirect(url_for("home"))
            else:
                error = "mot de passe incorrect"
                return render_template("login.html", error=error)
        else:
            error = "Nom d'utilisateur incorrect"
            return render_template("login.html", error=error)
    return render_template("login.html")


## LOGOUT ROUTE
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


## HOME ROUTE
@app.route("/")
def home():
    if not (current_user.is_authenticated):
        print(current_user.is_authenticated)
        return redirect(url_for("login"))
    else:
        return render_template("index.html")


def start():
    init_db()
    app.run(port=5000, debug=True, ssl_context="adhoc")


if __name__ == "__main__":
    start()
