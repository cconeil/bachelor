from flask import Flask, jsonify, send_from_directory
from flask_migrate import Migrate

from models import db
from models.models import Contestant

import os

app = Flask(__name__, static_url_path='/website/build/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.db.init_app(app)

migrate = Migrate(app, db.db)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("website/build/" + path):
        return send_from_directory('website/build', path)
    else:
        return send_from_directory('website/build', 'index.html')


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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
