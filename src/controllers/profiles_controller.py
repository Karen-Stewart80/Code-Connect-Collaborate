from flask import Blueprint, request, jsonify, abort
from schemas.ProfileSchema import profile_schema, profiles_schema
from models.Profiles import Profiles
from main import db

profiles = Blueprint("profiles", __name__, url_prefix="/profiles")

@profiles.route("/", methods=["GET"])
def profiles_index():
    profiles = Profiles.query.all()
    return jsonify(profiles_schema.dump(profiles))