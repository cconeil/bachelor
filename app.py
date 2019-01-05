from datetime import datetime
from datetime import timedelta

from flask import Flask, jsonify, send_from_directory
from flask_migrate import Migrate
from flask_cors import CORS

from models import db
from models.models import Contestant

import os

DB_FILENAME = "test.db"

app = Flask(__name__, static_url_path='/website/build/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(DB_FILENAME)
CORS(app)
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
                "num_followers": int(data_point.num_followers),
                "timestamp": data_point.timestamp,
                "contestant_id": data_point.contestant_id,
            })

        last_week_timestamp = datetime.now() - timedelta(days=7)
        yesterday_timestamp = datetime.now() - timedelta(days=1)

        results.append({
            "id": contestant.id,
            "name": contestant.name,
            "insta": contestant.insta,
            "image_url": contestant.image_url,
            "elimated_date": contestant.elimated_date,
            "is_slops_crew": contestant.is_slops_crew,
            "data_points": data_points,
            "delta_since_last_week": _delta_since(data_points, last_week_timestamp),
            "delta_since_yesterday": _delta_since(data_points, yesterday_timestamp)
        })
    results_with_followers = [result for result in results if len(result["data_points"])]
    sorted_results_with_followers = sorted(results_with_followers, key=lambda x: x["data_points"][-1]["num_followers"], reverse=True)
    results_without_followers = [result for result in results if not len(result["data_points"])]
    sorted_results_without_followers = sorted(results_without_followers, key=lambda x: x["name"])
    return jsonify(sorted_results_with_followers + sorted_results_without_followers)


def _delta_since(data_points, since_timestamp):
    if not len(data_points):
        return None

    first_data_point = data_points[-1]
    last_data_point = None
    for data_point in reversed(data_points):
        if data_point["timestamp"] < since_timestamp:
            last_data_point = data_point
            break

    if last_data_point is None:
        return None

    return (
        int(first_data_point["num_followers"]) - int(last_data_point["num_followers"])
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
