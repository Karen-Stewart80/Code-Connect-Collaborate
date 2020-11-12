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

    return jsonify(profile_schema.dump(new_user))

@profiles.route("/<string:username>", methods=["GET"])
def profiles_show(username):
    #Return a single user
    user = Profiles.query.filter_by(username = username).first()
    return jsonify(profile_schema.dump(user))

@profiles.route("/<string:username>", methods=["PUT", "PATCH"])
def profiles_update(username):
    #Update a user
    user = Profiles.query.filter_by(username = username)
    users_fields = profile_schema.load(request.json)
    user.update(users_fields)


    db.session.commit()

    return jsonify(profile_schema.dump(user[0]))

@profiles.route("/<int:userid>", methods=["DELETE"])
def profiles_delete(userid):
    #Delete a User
    users = Profiles.query.get(userid)
    db.session.delete(users)
    db.session.commit()

    return jsonify(profile_schema.dump(users))
