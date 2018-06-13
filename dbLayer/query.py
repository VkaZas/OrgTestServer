import redis

from dbLayer.index_encoding import *

r = redis.Redis(
    host='localhost',
    port=6379,
    password='')


def predict(gender, timeslot, province):
    encoding = index_encoding(gender, timeslot, province)
    return r.get(encoding).decode('utf-8')
