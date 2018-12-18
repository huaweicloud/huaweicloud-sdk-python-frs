# -*- coding: utf-8 -*-

from frscommon.frs_exception import FrsException


class HttpResponseUtils(object):

    @staticmethod
    def http_response2_result(resultClass, http_response):
        """Convert response to ordered result class"""
        if http_response is None:
            return None
        statusCode = http_response.status_code
        content = http_response.content
        if statusCode != 200:
            raise FrsException(statusCode, content)
        else:
            import sys
            if sys.version_info.major >= 3:
                content = str(content, encoding='utf-8')
            return resultClass(content)


class HttpRequestUtils(object):

    @staticmethod
    def load_file_as_multi_part(image_file):
        with open(image_file, 'rb') as f:
            binary = f.read()
        image_name = image_file.split('/')[-1].split('\\')[-1]
        return (image_name, binary)