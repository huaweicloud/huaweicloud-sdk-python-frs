# -*- coding: utf-8 -*-

import requests
import json
from requests.packages.urllib3 import encode_multipart_formdata
from frsaccess.apig_sdk import signer

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


class FrsAccess() :
    """Frs Access

    All http requests tools and signer

    """

    def __init__(self, auth_info, connection_timeout, connection_request_timeout, socket_timeout, proxies):
        self.auth_info = auth_info
        if connection_timeout and connection_request_timeout:
            self.timeout = (connection_timeout, connection_request_timeout)
        elif connection_timeout and (not connection_request_timeout):
            self.timeout = connection_timeout
        else:
            self.timeout = None
        self.proxies = proxies
        if socket_timeout:
            import socket
            socket.setdefaulttimeout(socket_timeout)


    def post(self, uri, request_body, is_file=False):
        self.sig = signer.Signer()
        self.sig.AppKey = self.auth_info.ak
        self.sig.AppSecret = self.auth_info.sk
        r = signer.HttpRequest()
        r.scheme, r.host = self.auth_info.end_point.split("://")
        r.method = "POST"
        r.uri = uri
        if is_file:
            if isinstance(request_body, dict):
                for k, v in request_body.items():
                    if isinstance(v, dict) or isinstance(v, list):
                        request_body[k] = str(v).replace('\'', '\"').replace('u\"', '\"')
            request_body, content_type = encode_multipart_formdata(request_body)
            r.headers = {"Content-Type": content_type}
        else:
            request_body = json.dumps(request_body)
            r.headers = {"Content-Type": "application/json"}
        r.body = request_body
        self.sig.Sign(r)
        response = requests.request(r.method, r.scheme+"://"+r.host+r.uri, headers=r.headers, data=r.body,
                                    verify=False, proxies=self.proxies, timeout=self.timeout)
        return response


    def get(self, uri):
        self.sig = signer.Signer()
        self.sig.AppKey = self.auth_info.ak
        self.sig.AppSecret = self.auth_info.sk
        r = signer.HttpRequest()
        r.scheme, r.host = self.auth_info.end_point.split("://")
        r.method = "GET"
        if "?" in uri:
            r.uri, query_tmp = uri.split("?")
            for kv in query_tmp.split("&"):
                k, v = kv.split("=")
                r.query[k] = v
        else:
            r.uri = uri
        self.sig.Sign(r)
        response = requests.request(r.method, r.scheme+"://"+r.host+r.uri, headers=r.headers, verify=False,
                                    proxies=self.proxies, timeout=self.timeout)
        return response


    def delete(self, uri):
        self.sig = signer.Signer()
        self.sig.AppKey = self.auth_info.ak
        self.sig.AppSecret = self.auth_info.sk
        r = signer.HttpRequest()
        r.scheme, r.host = self.auth_info.end_point.split("://")
        r.method = "DELETE"
        if "?" in uri:
            r.uri, query_tmp = uri.split("?")
            for kv in query_tmp.split("&"):
                k, v = kv.split("=")
                r.query[k] = v
        else:
            r.uri = uri
        self.sig.Sign(r)
        response = requests.request(r.method, r.scheme+"://"+r.host+r.uri, headers=r.headers, verify=False,
                                    proxies=self.proxies, timeout=self.timeout)
        return response
