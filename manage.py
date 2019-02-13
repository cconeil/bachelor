from flask_script import Manager
import requests
import time
import datetime
from models.models import Contestant, FollowerCountDataPoint
from models.db import db
from clients.instagram import Instagram

from app import app

manager = Manager(app)

account_id = 17841404349966033
token = 'EAAEeR6ST3pkBADSdXZBWIDsl9e0GbmKkN8wEd2iAbRmBAvECmoziS1wk2SMrgBsVWPCZCod01t9pBpQpjVvgzCDsoRrvZCFCynfc7dpskTSaztGQK6ZBkZAmBgQq1NxBhgZAXZBgMbA5PjzZCNxrsFqJvd5LldubIq4ZD'
url = "https://graph.facebook.com/v3.2/{}?fields=business_discovery.username({})%7Bfollowers_count%2Cmedia_count%7D&access_token={}"

@manager.command
def make_fake_data():
    print("starting")
    contestants = Contestant.query.all()
    for contestant in contestants:
        if len(contestant.data_points) == 0:
            continue
        datapoint = contestant.data_points[0]
        for i in range(0, 1000):
            new_timestamp = datapoint.timestamp + datetime.timedelta(hours=i)
            multiplier = (0.01 * i) + 1
            followers = int(float(datapoint.num_followers) * multiplier)
            new_datapoint = FollowerCountDataPoint(
                num_followers=followers, timestamp=new_timestamp
            )
            contestant.data_points.append(new_datapoint)
        db.session.add(contestant)
    db.session.commit()

    


def _get_follower_count(username, instagram):
    try:
        count = instagram.get_followers
        res = requests.get(url.format(account_id, username, token))
        print(res.json())
        return res.json()['business_discovery']['followers_count']
    except Exception as e:
        print('error', e)
        return None

@manager.command
def update_follower_counts():
    contestants = Contestant.query.all()
    instagram = Instagram()

    for contestant in contestants:
        follower_count_str = instagram.get_followers(contestant.insta)
        if follower_count_str == None:
            print("Something went wrong for", contestant.insta)
            continue

        follower_count = follower_count_str.replace(',', '')
        print(follower_count)

        data_point = FollowerCountDataPoint(
            num_followers=follower_count, timestamp=datetime.datetime.now()
        )
        contestant.data_points.append(data_point)
        db.session.add(contestant)

    db.session.commit()

@manager.command
def load_insta():
    instagram = Instagram()
    instagram.load_site()

if __name__ == "__main__":
    manager.run()



# 1|52619|2019-01-05 21:46:57.988175
# 2|6524|2019-01-05 21:46:59.395076
# 3|1504|2019-01-05 21:47:00.215376
# 4|39517|2019-01-05 21:47:01.477699
# 5|4250|2019-01-05 21:47:02.815686
# 6|2746|2019-01-05 21:47:04.362842
# 7|37346|2019-01-05 21:47:05.488574
# 8|13203|2019-01-05 21:47:06.870281
# 9|2930|2019-01-05 21:47:08.010948
# 10|1593|2019-01-05 21:47:09.168355
# 11|7939|2019-01-05 21:47:10.443619
# 12|5780|2019-01-05 21:47:11.703964
# 13|3553|2019-01-05 21:47:12.971526
# 14|76659|2019-01-05 21:47:14.274292
# 15|2493|2019-01-05 21:47:15.550568
# 16|6050|2019-01-05 21:47:16.983851
# 17|2936|2019-01-05 21:47:18.357465
# 18|4632|2019-01-05 21:47:19.617932
# 19|1834|2019-01-05 21:47:20.759470
# 20|2395|2019-01-05 21:47:22.044238
# 21|9904|2019-01-05 21:47:23.187490
# 22|5280|2019-01-05 21:47:24.445110
# 23|2710|2019-01-05 21:47:25.788060
# 24|5016|2019-01-05 21:47:27.080742
# 25|2415|2019-01-05 21:47:28.393843
# 26|2335|2019-01-05 21:47:32.240118
# 27|1062|2019-01-05 21:47:33.458042
# 28|14116|2019-01-05 21:47:34.888578
# 29|3222|2019-01-05 21:47:36.127093