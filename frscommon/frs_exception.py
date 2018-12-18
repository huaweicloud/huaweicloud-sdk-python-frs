# -*- coding: utf-8 -*-

class FrsException(Exception):
    def __init__(self, http_status_code, msg):
        super(Exception, self).__init__("{\"http_code\": %s, \"msg\": \"%s\"}" % (http_status_code, msg))
