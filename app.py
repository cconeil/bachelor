from flask import Flask, jsonify
from flask_migrate import Migrate

from models import db
from models.models import Contestant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.db.init_app(app)

migrate = Migrate(app, db.db)


@app.route('/')
def hello_world():
    return 'Hello all users!'


@app.route('/update/')
def return_everything():
    contestants = Contestant.query.all()
    return jsonify(contestants)
