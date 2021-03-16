from flask_restful import Resource


class Player(Resource): # add player
    @classmethod
    def post(cls):
        pass

    @classmethod # get player by name
    def get_player(cls):
        pass

    @classmethod  # add or amend player
    def put(cls):
        pass

    @classmethod # delete player
    def delete(cls):
        pass


class PlayerList(Resource): # list all players
    @classmethod
    def get_all_players(cls):
        pass


class TeamList(Resource):
    @classmethod # list all players by team
    def get_players_by_team(cls):
        pass


class NationList(Resource):
    @classmethod # list all players by their nationality
    def get_players_by_nation(cls):
        pass



