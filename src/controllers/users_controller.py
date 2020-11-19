from flask import Blueprint
from schemas.UsersSchema import user_schema, users_schema
from flask import Blueprint, request, jsonify, abort
from models.Users import Users
from main import bcrypt, db
from flask_jwt_extended import create_access_token
from datetime import timedelta

auth = Blueprint('auth', __name__, url_prefix="/auth")

@auth.route("/register", methods=["POST"])
def auth_register():
    user_fields = user_schema.load(request.json)

    user = Users.query.filter_by(email=user_fields["email"]).first()

    if user:
        return abort(400, description="User already")
    
    user = Users()
    user.email = user_fields["email"]
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")

    db.session.add(account)
    db.session.commit()

    return jsonify(user_schema.dump(user))


@auth.route("/login", methods=["POST"])
def auth_login():
    user_fields = user_schema.load(request.json)

    user = Users.query.filter_by(email=user_fields["email"]).first()

    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return abort(401, description="Incorrect username and password")

    expiry = timedelta(days=1)
    access_token = create_access_token(identity=str(account.id), expires_delta=expiry)

    return jsonify({ "token": access_token })