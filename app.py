from flask import Flask

from models import db
from models.models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.db.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello all users {}'.format(User.query.all())
