from flask import Flask
from flask import request
import json

from model_util import load_model
from predictor import predict, validate_attrs

app = Flask(__name__)
load_model()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/testapi', methods=['GET'])
def test_api():
    params = {
        'time': request.args.get('time'),
        'sex': request.args.get('sex'),
        'province': request.args.get('province'),
    }

    if not validate_attrs(params):
        return json.dumps({
            'prize': [],
            'prob': [],
            'status': 'Failed',
        })

    result_prize, result_prob = predict(params)
    return json.dumps({
        'prize': result_prize,
        'prob': result_prob,
        'status': 'Succeeded',
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0')

