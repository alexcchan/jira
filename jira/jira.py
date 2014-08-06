"""
   Wrapper for the JIRA API.  Based on the Python Zendesk library by Max
   Gutman <max@eventbrite.com>.
"""


import base64
import httplib2
import re
import urllib
try:
    import simplejson as json
except:
    import json

from endpoints_v2 import mapping_table as mapping_table_v2
from httplib import responses


DEFAULT_HTTP_METHOD = 'GET'
DEFAULT_HTTP_STATUS_CODE = 200
DEFAULT_CONTENT_TYPE = 'application/json'


class JiraError(Exception):
    def __init__(self, msg, error_code=None):
        self.msg = msg
        self.error_code = error_code

    def __str__(self):
        return repr('%s: %s' % (self.error_code, self.msg))


def clean_kwargs(kwargs):
    for key, value in kwargs.iteritems():
        if hasattr(value, '__iter__'):
            kwargs[key] = ','.join(map(str, value))
    underscore_keys = [key for key in kwargs if key.find('_')>=0]
    for key in underscore_keys:
        val = kwargs.pop(key)
        kwargs[key.replace('_','-')] = val


class Jira(object):

    def __init__(self, jira_url, jira_username=None, jira_password=None, api_version=2):
        self.jira_url = jira_url
        self.jira_username = jira_username
        self.jira_password = jira_password
        if api_version == 2:
            self.mapping_table = mapping_table_v2
        else:
            raise ValueError("Unsupported JIRA API Version: %d" %
                    api_version)
        self.client = httplib2.Http()

    def __getattr__(self, api_call):
        def call(self, **kwargs):
            api_map = self.mapping_table[api_call]
            path = self.mapping_table.get('path_prefix','') + api_map.get('path','')
            method = api_map.get('method', DEFAULT_HTTP_METHOD)
            status = api_map.get('status', DEFAULT_HTTP_STATUS_CODE)
            valid_params = api_map.get('valid_params', [])
            body = kwargs.pop('data', None)
            url = re.sub(
                    '\{\{(?P<m>[a-zA-Z_]+)\}\}',
                    lambda m: "%s" % urllib.quote(str(kwargs.pop(m.group(1),''))),
                    self.jira_url + path
            )
            clean_kwargs(kwargs)
            for kw in kwargs:
                if kw not in valid_params:
                    raise TypeError("%s() got an unexpected keyword argument "
                            "'%s'" % (api_call, kw))
            url += '?' + urllib.urlencode(kwargs)
            return self._make_request(method, url, body, status)
        return call.__get__(self)

    def _make_request(self, method, url, body, status):
        headers = {}
        headers["Authorization"] = "Basic %s" % (
                base64.b64encode(self.jira_username + ':' + self.jira_password))
        if body:
            content_type = self.mapping_table.get('content_type', DEFAULT_CONTENT_TYPE)
            headers["Content-Type"] = content_type
            if isinstance(body, dict):
                if content_type == 'application/x-www-form-urlencoded':
                    body = urllib.urlencode(body)
                elif content_type == 'application/json':
                    body = json.dumps(body)
                else:
                    # TODO throw error
                    pass
        response,content = self.client.request(url, method=method, body=body,
                headers=headers)
        return self._response_handler(response, content, status)

    def _response_handler(self, response, content, status):
        if not response:
            raise JiraError('Response Not Found')
        response_status = int(response.get('status', 0))
        if response_status != status:
            raise JiraError(content, response_status)
        if response.get('location'):
            return response.get('location')
        elif content.strip():
            return json.loads(content)
        else:
            return responses[response_status]
