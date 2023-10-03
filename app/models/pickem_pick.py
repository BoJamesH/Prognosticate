from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Pickem_Pick(db.Model):
    __tablename__ = 'pickem_picks'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    week = db.Column(db.Integer)
    game_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('games.id')))
    selected_team_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')))
    open = db.Column(db.Boolean)
    win = db.Boolean(db.Boolean)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'week': self.week,
            'game_id': self.game_id,
            'selected_team_id': self.selected_team_id,
            'open': self.open,
            'win': self.win,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
