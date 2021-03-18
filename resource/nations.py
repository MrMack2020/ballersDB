from flask_restful import Resource


class Nations(Resource): # find specific nation
    @classmethod
    def get(cls):
        pass


class NationList(Resource):
    @classmethod # list all nations
    def get(cls):
        pass