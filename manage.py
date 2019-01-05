import shutil

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
BACKUP_DIRECTORY = "../backups/bachelor/"
DB_FILENAME = "test.db"

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

@manager.command
def backup_db():
    shutil.copyfile(DB_FILENAME, BACKUP_DIRECTORY + DB_FILENAME)

if __name__ == "__main__":
    manager.run()
