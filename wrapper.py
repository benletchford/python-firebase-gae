import urllib
import json
from google.appengine.api import urlfetch


class Firebase(object):

    def __init__(self, root_url, auth_token):
        self.root_url = root_url
        self.auth_token = auth_token

    # The methods set, push, update and remove are intended to mimic Firebase
    # API calls.

    def set(self, payload):
        return self.put(payload)

    def push(self, payload):
        return self.post(payload)

    def update(self, payload):
        return self.patch(payload)

    def remove(self):
        return self.delete()

    def get(self):
        return self._request(urlfetch.GET)

    def post(self, payload):
        return self._request(urlfetch.POST, payload=payload)

    def put(self, payload):
        return self._request(urlfetch.PUT, payload=payload)

    def patch(self, payload):
        return self._request(urlfetch.PATCH, payload=payload)

    def delete(self):
        return self._request(urlfetch.DELETE)

    def _request(self, method, **kwargs):
        if 'payload' in kwargs:
            kwargs['payload'] = json.dumps(kwargs['payload'])

        params = {}
        if 'params' in kwargs:
            params.update(kwargs['params'])
            del kwargs['params']

        if self.auth_token:
            params.update({'auth': self.auth_token})

        # Do we need to chuck on some extra params?
        if params:
            url = '%s?%s' % (self.root_url, urllib.urlencode(params))
        else:
            url = self.root_url

        response = urlfetch.fetch(url, method=method, **kwargs)

        return json.loads(response.content)
