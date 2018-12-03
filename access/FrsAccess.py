# _*_ coding: utf-8 _*_

import requests
import json
import urllib3
from urllib3 import encode_multipart_formdata
from .apig_sdk import signer

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class FrsAccess() :
    """Frs Access

    All http requests tools, and signer

    """

    def __init__(self, authInfo, connectionTimeout, connectionRequestTimeout, socketTimeout, proxies):
        self.authInfo = authInfo
        if connectionTimeout and connectionRequestTimeout:
            self.timeout = (connectionTimeout, connectionRequestTimeout)
        elif connectionTimeout and (not connectionRequestTimeout):
            self.timeout = connectionTimeout
        else:
            self.timeout = None
        self.proxies = proxies
        if socketTimeout:
            import socket
            socket.setdefaulttimeout(socketTimeout)

    def post(self, uri, requestBody, isFile=False):
        self.sig = signer.Signer()
        self.sig.AppKey = self.authInfo.ak
        self.sig.AppSecret = self.authInfo.sk
        r = signer.HttpRequest()
        r.scheme, r.host = self.authInfo.endPoint.split("://")
        r.method = "POST"
        r.uri = uri
        if isFile:
            if isinstance(requestBody, dict):
                for k, v in requestBody.items():
                    if isinstance(v, dict) or isinstance(v, list):
                        requestBody[k] = str(v).replace('\'', '\"').replace('u\"', '\"')
            requestBody, contentType = encode_multipart_formdata(requestBody)
            r.headers = {"Content-Type": contentType}
        else:
            requestBody = json.dumps(requestBody)
            r.headers = {"Content-Type": "application/json"}
        r.body = requestBody
        self.sig.Sign(r)
        response = requests.request(r.method, r.scheme+"://"+r.host+r.uri, headers=r.headers, data=r.body, verify=False,
            proxies=self.proxies, timeout=self.timeout)
        return response


    def get(self, uri):
        self.sig = signer.Signer()
        self.sig.AppKey = self.authInfo.ak
        self.sig.AppSecret = self.authInfo.sk
        r = signer.HttpRequest()
        r.scheme, r.host = self.authInfo.endPoint.split("://")
        r.method = "GET"
        if "?" in uri:
            r.uri, query_tmp = uri.split("?")
            for kv in query_tmp.split("&"):
                k, v = kv.Split("=")
                r.query[k] = v
        else:
            r.uri = uri
        self.sig.Sign(r)
        response = requests.request(r.method, r.scheme+"://"+r.host+r.uri, headers=r.headers, verify=False,
            proxies=self.proxies, timeout=self.timeout)
        return response


    def delete(self, uri):
        self.sig = signer.Signer()
        self.sig.AppKey = self.authInfo.ak
        self.sig.AppSecret = self.authInfo.sk
        r = signer.HttpRequest()
        r.scheme, r.host = self.authInfo.endPoint.split("://")
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
