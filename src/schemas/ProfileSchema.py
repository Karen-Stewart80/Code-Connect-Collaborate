from main import ma
from models.Profiles import Profiles
from marshmallow.validate import Length

class ProfileSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Profiles
    username = ma.String(required=True, validate=Length(min=1))
    fname = ma.String(required=True, validate=Length(min=1))
    lname = ma.String(required=True, validate=Length(min=1))
    userpass = ma.String(required=True, validate=Length(min=1))
    profile_pic = ma.String(required=False)
    account_active = ma.Boolean(required=True)
    email = ma.String(required=True, validate=Length(min=1))
    github = ma.String(required=False, validate=Length(min=1))

profile_schema = ProfileSchema()
profiles_schema = ProfileSchema(many=True)