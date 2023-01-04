import json


def do_json_request(session, url, method, data={}):
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response = session.request(url=url, method=method, data=json.dumps(data), headers=headers)
    if response.status_code < 200 or response.status_code >= 300:
        raise Exception({response.text, response.status_code})
    return response
