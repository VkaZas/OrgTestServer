import requests
import json

url_query = "http://127.0.0.1:5000/testapi"

parameter = {
    "timeslot": '09',
    "gender": '1',
    "province": '新疆'
}

response = requests.get(url_query, parameter)

data = json.loads(bytes.decode(response.content, 'utf-8'))

print (data)