from flask_restful import Resource


class PlayerNames(Resource): # add player
    @classmethod
    def post(cls):
        pass

    @classmethod # get player by name
    def get(cls):
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





