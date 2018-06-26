import json

from flask import Flask
from flask import request

from redisLayer.query import predict
from redisLayer.load_json_to_redis import load_json_to_redis

from mongoLayer.query import update_customer_prize_record, update_customer_participation_record

from utils import prizeid_sourceid_dict

app = Flask(__name__)
load_json_to_redis()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/prizeLogUpdate', methods=['POST'])
def prizeLogUpdate():
    try:
        timestamp = request.form.get('timestamp')
        gender = request.form.get('gender')
        province = request.form.get('province')
        prizeid = request.form.get('prizeid')
        openid = request.form.get('openid')
        city = request.form.get('city')
        qrcode = request.form.get('qrcode')

        update_customer_prize_record(openid, gender, province, city, prizeid, qrcode, timestamp)
        return json.dumps({
            'status': 'success',
        })

    # any possible error go on
    except Exception as e:
        error = {
            "message": str(e)
        }
        return json.dumps(error)


@app.route('/interfaceLogUpdate', methods=['POST'])
def interfaceLogUpdate():
    try:
        timestamp = request.form.get('timestamp')
        prizeid = request.form.get('prizeid')
        openid = request.form.get('openid')

        update_customer_participation_record(openid, prizeid, timestamp)
        return json.dumps({
            'status': 'success',
        })

    # any possible error go on
    except Exception as e:
        error = {
            "message": str(e)
        }
        return json.dumps(error)


@app.route('/predict', methods=['POST'])
def test_api():
    try:
        projectid = request.form.get('projectid')
        gender = request.form.get('gender')
        city = request.form.get('city')
        prizeid_list = json.loads(request.form.get('prizeid_list'))

        # Convert prizeid_list to sourceid_list and save the projection
        sourceid_prizeid_temp_dict = {}
        for prizeid in prizeid_list:
            sourceid = prizeid_sourceid_dict.get(prizeid)
            if sourceid is not None:
                sourceid_prizeid_temp_dict[sourceid] = prizeid

        # must be json
        product_and_probability = json.loads(predict(projectid, city, gender))

        # Convert sourceid_list to prizeid_list back via saved projection
        # Reverse loop for safe deleting elements
        for i in range(len(product_and_probability))[::-1]:
            item = product_and_probability[i]
            sourceid = item.get('id')
            isExist = sourceid_prizeid_temp_dict.get(sourceid) is not None
            if isExist:
                item['id'] = sourceid_prizeid_temp_dict.get(sourceid)
            else:
                product_and_probability.remove(item)

        return json.dumps(product_and_probability)

    # any possible error go on
    except Exception as e:
        error = {
            "message": str(e)
        }
        return json.dumps(error)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
