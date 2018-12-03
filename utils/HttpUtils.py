# _*_ coding: utf-8 _*_

from common.FrsException import FrsException

class HttpResponseUtils(object):

    @staticmethod
    def httpResponse2Result(resultClass, httpResponse):
        """Convert response to ordered result class"""
        if httpResponse is None:
            return None
        statusCode = httpResponse.status_code
        content = httpResponse.content
        if statusCode != 200:
            raise FrsException(statusCode, content)
        else:
            import sys
            if sys.version_info.major >= 3:
                content = str(content, encoding='utf-8')
            return resultClass(content)

class HttpRequestUtils(object):

    @staticmethod
    def loadFileAsMultiPart(imagePath):
        with open(imagePath, 'rb') as f:
            binary = f.read()
        imageName = imagePath.split('/')[-1].split('\\')[-1]
        return (imageName, binary)