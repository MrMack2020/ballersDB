"""
this an app that will put classic football players of the past into a database with numerous categories
that can be used to show the players to a user.  There will be three nationality zones (stores), and several
stats columns, registration and logins
"""
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from BallerDB import db

app = Flask(__name__)
app.secret_key = "macca"
api = Api(app)


@app.before_first_request
def create_table():
    db.create_all()


jwt = JWTManager(app)


app.add_resource (UserRegister, '/register')


if __name__ == "__main__":
    db.init.app(app)
    app.run(port=5000, debug=True)








