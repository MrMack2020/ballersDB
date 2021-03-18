"""
this an app that will put classic football players of the past into a database with numerous categories
that can be used to show the players to a user.  There will be three nationality zones (stores), and several
stats columns, registration and logins
"""
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from BallerDB import db
from resource.player import PlayerNames


app = Flask(__name__)
app.secret_key = "macca"
api = Api(app)


@app.before_first_request
def create_table():
    db.create_all()


jwt = JWTManager(app)


app.add_resource(UserRegister, '/register')
app.add_resource(UserLogin, '/login')
app.add_resource(User, '/user/<string:name>')
app.add_resource(UserLogout, '/logout')
app.add_resource(Playersnames, '/player/<string:name>')
app.add_resource(PlayerList, '/players')
app.add_resource(TeamList, '/find/<string:name>')
app.add_resource(NationList, '/find/<string:name>')
app.add_resource(TeamList, '/teams')
app.add_resource(TeamFind, '/team/<string:name')
app.add_resource(NationList, '/nations')
app.add_resource(Nation, '/nation/<string:name')


if __name__ == "__main__":
    db.init.app(app)
    app.run(port=5000, debug=True)








