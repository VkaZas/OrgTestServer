import redis
import json

r = redis.Redis(
    host='localhost',
    port=6379,
    password='')

# Empty db
r.flushall()

# load data into redis
with open('data.json') as f:
    data = json.load(f)

for entry in data:
    key = entry["key"]
    value = json.dumps(entry["value"])
    r.set(key, value)


