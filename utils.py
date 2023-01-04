import json
import uuid


MENTION_NODE_NAME = 'span'
MENTION_ID_PREFIX = 'mention-'
MENTION_CLASS = 'mention'


def do_json_request(session, url, method, data=None):
    if data is None:
        data = {}
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response = session.request(url=url, method=method, data=json.dumps(data), headers=headers)
    if response.status_code < 200 or response.status_code >= 300:
        raise Exception({response.text, response.status_code})
    return response


def wrap_in_mention_node(text: str):
    if text == "":
        return ""
    return f'<{MENTION_NODE_NAME} id="{MENTION_ID_PREFIX}{uuid.uuid4()}" class="{MENTION_CLASS}">' + \
           f'@{text}</{MENTION_NODE_NAME}>'
