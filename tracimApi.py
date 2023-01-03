import json
import requests

from .utils import do_json_request


class TracimApi:
    api_url: str
    token: str

    def __init__(self, host: str, protocol="http", port="80"):
        self.api_url = f"{protocol}://{host}:{port}"
        self.session = requests.Session()

    def auth(self, email: str, password: str):
        url = f"{self.api_url}/api/auth/login"
        data = {"email": email, "password": password}
        do_json_request(self.session, url, "post", data=data)
        if "session_key" not in self.session.cookies.get_dict():
            raise f"Could not read session_cookie"
        self.token = self.session.cookies.get_dict()['session_key']

    def get_workspaces(self):
        url = f"{self.api_url}/api/workspaces"
        response = do_json_request(self.session, url, "get")
        return json.loads(response.text)

    def get_contents_of_workspace(self, workspace_id: str):
        url = f"{self.api_url}/api/workspaces/{workspace_id}/contents"
        response = do_json_request(self.session, url, "get")
        return json.loads(response.text)

    def post_comment(self, workspace_id, content_id, comment):
        url = f"{self.api_url}/api/workspaces/{workspace_id}/contents/{content_id}/comments"
        data = {"raw_content": comment}
        do_json_request(self.session, url, "post", data=data)
