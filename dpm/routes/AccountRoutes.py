from env import get_version
from flask import Blueprint, jsonify, render_template, request
from services.AccountService import (
    create_account_service,
    delete_account_service,
    get_account_by_id_service,
    get_all_accounts_service,
    update_account_service,
)

accounts_bp = Blueprint("accounts", __name__)
version = get_version()


@accounts_bp.route(f"/api/{version}/accounts", methods=["GET", "POST"])
def get_accounts():
    accounts = get_all_accounts_service()
    accounts_list = [account.to_dict() for account in accounts]
    if request.method == "POST":
        print(1)
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        if not username or not password or not email:
            error = "username and password and email required"
            return render_template("account.html", data=accounts_list, error=error)
        else:
            new_account_id = create_account_service(username, password, email)
            new_account = get_account_by_id_service(new_account_id)
            accounts_list.append(new_account.to_dict())
    return render_template("account.html", data=accounts_list)


@accounts_bp.route(f"/api/{version}/accounts/<int:user_id>", methods=["GET"])
def get_account_by_id_route(user_id):
    account = get_account_by_id_service(user_id)
    if account:
        account_dict = account.to_dict()
        return jsonify({"account": account_dict})
    else:
        return jsonify({"error": f"account with user_id = {user_id} not found"}), 404


@accounts_bp.route(f"/api/{version}/accounts/<int:user_id>", methods=["PUT"])
def update_account_route(user_id):
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    if not username and not password and not email:
        return jsonify({"error": "username or password or email required"}), 400
    else:
        existing_account = get_account_by_id_service(user_id)
        if existing_account:
            if not username:
                username = existing_account.username
            if not email:
                email = existing_account.email
            if not password:
                password = existing_account.password
            update_account_service(user_id, username, password, email)
            return jsonify({"message": "account updated succesfully", "user_id": user_id})
        else:
            return jsonify({"error": "account not found"}), 404


@accounts_bp.route(f"/api/{version}/accounts/<int:user_id>", methods=["DELETE"])
def delete_account_route(user_id):
    existing_account = get_account_by_id_service(user_id)
    if existing_account:
        delete_account_service(user_id)
        return jsonify({"message": "account deleted succesfully", "user_id": user_id})
    else:
        return jsonify({"error": "account not found"}), 404
