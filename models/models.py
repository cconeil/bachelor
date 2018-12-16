from models.db import db


class Contestant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    insta = db.Column(db.String(256), nullable=False)
    image_url = db.Column(db.String(512), nullable=False)
    elimated_date = db.Column(db.DateTime, nullable=True)
    is_slops_crew = db.Column(db.Boolean)
    data_points = db.relationship(
        'FollowerCountDataPoint', backref='user', lazy=True
    )

    def __unicode__(self):
        return '<User %r>' % self.id

    def __repr__(self):
        return '<User %r>' % self.id


class FollowerCountDataPoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_followers = db.Column(db.String(256), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=True)
    contestant_id = db.Column(
        db.Integer, db.ForeignKey('contestant.id'), nullable=False
    )

    def __unicode__(self):
        return '<User %r>' % self.id

    def __repr__(self):
        return '<User %r>' % self.id
