import redis

from redisLayer.index_encoding import *

r = redis.Redis(
    host='localhost',
    port=6379,
    password='')


def predict(projectid, city, gender):
    encoding = index_encoding(projectid, city, gender)
    return r.get(encoding).decode('utf-8')
