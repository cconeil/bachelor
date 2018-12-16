import db

class User(db.db.Model):
    id = db.db.Column(db.db.Integer, primary_key=True)
    # id = db.Column(
    #     db.UUID(as_uuid=True), unique=True, nullable=False, primary_key=True
    # )

    # username = db.Column(db.String(80), unique=True, nullable=False)
    # email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id
