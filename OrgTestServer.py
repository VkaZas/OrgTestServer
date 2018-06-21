import json

from flask import Flask
from flask import request

from redisLayer.query import predict
from redisLayer.load_json_to_redis import load_json_to_redis

from mongoLayer.query import update_customer_prize_record, update_customer_participation_record


app = Flask(__name__)
load_json_to_redis()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/prizeLogUpdate', methods=['POST'])
def prizeLogUpdate():
    try:
        timestamp = request.args.get('timestamp')
        gender = request.args.get('gender')
        province = request.args.get('province')
        prizeid = request.args.get('prizeid')
        openid = request.args.get('openid')

        update_customer_prize_record(openid, gender, province, prizeid, timestamp)

    # any possible error go on
    except Exception as e:
        error = {
            "message": str(e)
        }
        return json.dumps(error)


@app.route('/interfaceLogUpdate', methods=['POST'])
def interfaceLogUpdate():
    try:
        timestamp = request.args.get('timestamp')
        prizeid = request.args.get('prizeid')
        openid = request.args.get('openid')

        update_customer_participation_record(openid, prizeid, timestamp)

    # any possible error go on
    except Exception as e:
        error = {
            "message": str(e)
        }
        return json.dumps(error)


@app.route('/testapi', methods=['GET'])
def test_api():
    try:
        timeslot = request.args.get('timeslot')
        gender = request.args.get('gender')
        province = request.args.get('province')

        # must be json
        product_and_probability = predict(gender, timeslot, province)
        return product_and_probability

    # any possible error go on
    except Exception as e:
        error = {
            "message": str(e)
        }
        return json.dumps(error)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
