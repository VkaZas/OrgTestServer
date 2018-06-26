import datetime
from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'customer_records',
    'host': '127.0.0.1',
    'port': 27017,
}
db = MongoEngine(app)


class Record(db.EmbeddedDocument):
    timestamp = db.DateTimeField(required=True, default=datetime.datetime.utcnow)
    prizeid = db.StringField(required=True)
    participation = db.BooleanField(required=True, default=False)
    qrcode = db.StringField(required=True)


class Customer(db.Document):
    openid = db.StringField(required=True)
    province = db.StringField(required=True)
    city = db.StringField(required=True)
    gender = db.IntField(required=True)
    records = db.ListField(db.EmbeddedDocumentField('Record'))
