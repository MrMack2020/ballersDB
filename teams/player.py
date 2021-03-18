from flask_restful import Resource


class TeamFind(Resource):
    @classmethod # list all players by team
    def find_team(cls):
        pass

class TeamList(Resource):
    @classmethod
    def get_all_teams(cls): # show all teams in db
        pass