import urllib
import json
import requests

url_endpoint = 'http://write_event:6000/events'

def write_event(arg1,arg2):
#def read_event(request_parapms):
    body = {
    'pod_id':arg1,
    'msg':arg2
    }

    #content = requests.get(url=url_endpoint, params = request_parapms)
    content = requests.post(url=url_endpoint, params = body)
    #content = requests.get(url=url_endpoint)
    print('response from write-tire: ', content.json())
    return str(content.json())
    #return jsonify({'message': string, 'random' : json.loads(content)['message']})
