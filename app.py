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

    results = []
    for contestant in contestants:
        data_points = []
        for data_point in contestant.data_points:
            data_points.append({
                "id": data_point.id,
                "num_followers": data_point.num_followers,
                "timestamp": data_point.timestamp,
                "contestant_id": data_point.contestant_id,
            })

        results.append({
            "id": contestant.id,
            "name": contestant.name,
            "insta": contestant.insta,
            "image_url": contestant.image_url,
            "elimated_date": contestant.elimated_date,
            "is_slops_crew": contestant.is_slops_crew,
            "data_points": data_points
        })

    return jsonify(results)
