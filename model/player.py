from typing import list
from BallersDB import db


class PlayerModel(db.Model):
    __tablename__ = 'Players'

    first_name = db.Column(db.String(15), )
    surname = db.Column(db.String(30), nullable=False)
    nationality = db.Column(db.String(25), nullable=False)
    club_trophies = db.Column(db.Integer)
    team_trophies = db.Column(db.Integer)

class Team(db.Model):
    pass


