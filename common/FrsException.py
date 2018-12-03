# _*_ coding: utf-8 _*_

class FrsException(Exception):
    def FrsException(self, httpStatusCode, msg):
        Exception.__init__("{\"http_code\": %s, \"msg\": \"%s\"}"%(httpStatusCode, msg))