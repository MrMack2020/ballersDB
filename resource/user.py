from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required,
    get_jwt,
    create_access_token,
    create_refresh_token
)


class UserRegister(Resource):
    @classmethod # /register
    def post(cls):
        pass


class UserLogin(Resource):
    @classmethod  # /login
    def post(cls):
        pass


class User(Resource):
    @classmethod # find user
    @jwt_required
    def get(cls):
        pass

    @classmethod # delete user
    @jwt_required
    def delete(cls):
        pass


class UserLogout(Resource):
    @classmethod # /logout
    def post(cls):
        pass


