from flask import Blueprint, request, jsonify, abort
from schemas.ProfileSchema import profile_schema, profiles_schema
from models.Profiles import Profiles
from main import db

profiles = Blueprint("profiles", __name__, url_prefix="/profiles")

@profiles.route("/", methods=["GET"])
def profiles_index():
    profiles = Profiles.query.all()
    return jsonify(profiles_schema.dump(profiles))


@profiles.route("/", methods=["POST"])
def profiles_create():
    users_fields = profile_schema.load(request.json)

    new_user = Profiles()
    new_user.username = users_fields["username"]
    new_user.fname = users_fields["fname"]
    new_user.lname = users_fields["lname"]
    new_user.userpass = users_fields["userpass"]
    new_user.profile_pic = users_fields["profile_pic"]
    new_user.account_active = users_fields["account_active"]
    new_user.email = users_fields["email"]
    new_user.github = users_fields["github"]

    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_schema.dump(new_user))