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
        for data_point in filtered_points(contestant.data_points, 'week'):
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
            "delta": _delta(data_points),
        })

    results_with_followers = [result for result in results if len(result["data_points"])]
    sorted_results_with_followers = sorted(results_with_followers, key=lambda x: x["data_points"][-1]["num_followers"], reverse=True)
    results_without_followers = [result for result in results if not len(result["data_points"])]
    sorted_results_without_followers = sorted(results_without_followers, key=lambda x: x["name"])
    return jsonify(sorted_results_with_followers + sorted_results_without_followers)


def _delta(data_points):
    if len(data_points) < 2:
        return None

    return (
        int(data_points[-1]['num_followers']) - int(data_points[0]['num_followers'])
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


def filtered_points(data_points, filters):
    now = datetime.now()
    one_day_ago = now - timedelta(days=1)
    one_week_ago = now - timedelta(days=7)
    one_month_ago = now - timedelta(days=30)

    filtered_data_points = []

    for data_point in data_points:
        time = data_point.timestamp
        if filters == 'day' and time > one_day_ago and time < now:
            filtered_data_points.append(data_point)
        elif filters == 'week' and time > one_week_ago and time < now and time.hour == 4:
            filtered_data_points.append(data_point)
        elif filters == 'month' and time > one_month_ago and time < now and time.hour == 4:
            filtered_data_points.append(data_point)
        elif filters == 'all' and time.hour == 4:
            filtered_data_points.append(data_point)
    
    return filtered_data_points
