import requests
import time
import datetime

from models.models import Contestant, FollowerCountDataPoint
from models.db import db

account_id = 17841404349966033
token = 'EAAEeR6ST3pkBADSdXZBWIDsl9e0GbmKkN8wEd2iAbRmBAvECmoziS1wk2SMrgBsVWPCZCod01t9pBpQpjVvgzCDsoRrvZCFCynfc7dpskTSaztGQK6ZBkZAmBgQq1NxBhgZAXZBgMbA5PjzZCNxrsFqJvd5LldubIq4ZD'
url = "https://graph.facebook.com/v3.2/{}?fields=business_discovery.username({})%7Bfollowers_count%2Cmedia_count%7D&access_token={}"


def _get_follower_count(username):
    try:
        res = requests.get(url.format(account_id, username, token))
        print(res.json())
        return res.json()['business_discovery']['followers_count']
    except Exception as e:
        print('error', e)
        return None


def update_follower_counts():
    contestants = Contestant.query.all()

    for contestant in contestants:
        follower_count = _get_follower_count(contestant.insta)
        if follower_count:
            data_point = FollowerCountDataPoint(
                num_followers=follower_count, timestamp=datetime.datetime.now()
            )
            contestant.data_points.append(data_point)
            db.session.add(contestant)

    db.session.commit()


update_follower_counts()
