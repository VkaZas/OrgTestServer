import json

from flask import Flask
from flask import request

from dbLayer.query import predict
from dbLayer.load_json_to_redis import load_json_to_redis

app = Flask(__name__)
load_json_to_redis()


@app.route('/')
def hello_world():
    return 'Hello World!'


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
