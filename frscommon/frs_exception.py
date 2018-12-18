# -*- coding: utf-8 -*-

class FrsException(Exception):
    def frs_exception(self, http_status_code, msg):
        super(Exception, self).__init__("{\"http_code\": %s,\n\"msg\": \"%s\"}" % (http_status_code, msg))
