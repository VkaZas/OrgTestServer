import redis
import json
import os
from redisLayer.index_encoding import filename_projectid_dict


def load_json_to_redis():
    r = redis.Redis(
        host='localhost',
        port=6379,
        password='')

    # Empty db
    r.flushall()

    # load data into redis
    for dirpath, _, filenames in os.walk('redisLayer/data'):
        for file in filenames:
            projectid = filename_projectid_dict[file]
            fullpath = os.path.join(dirpath, file)
            with open(fullpath) as f:
                data = json.load(f)

            for entry in data:
                key = projectid + '_' + entry["key"]
                value = json.dumps(entry["value"])
                r.set(key, value)






