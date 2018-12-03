# _*_ coding: utf-8 _*_

from utils import HttpUtils
from common import FrsConstant
from common import ImageType
from ..result import DetectFaceResult

class DetectService(object):

    def __init__(self, service, projectId):
        """Init
        :param service:
        :type service: FrsAccess
        """
        self.service = service
        self.projectId = projectId

    def _detectFace(self, image, imageType, attributes):
        """
        :rtype: DetectFaceResult
        """
        uri = FrsConstant.faceDetectUri % self.projectId
        requestBody = {}
        if attributes:
            requestBody['attributes'] = attributes
        if imageType == ImageType.BASE64:
            if type(image) is bytes:
                requestBody['image_base64'] = image.decode()
            else:
                requestBody['image_base64'] = image
        elif imageType == ImageType.OBSURL:
            requestBody['image_url'] = image
        elif imageType == ImageType.FILE:
            requestBody['image_file'] = HttpUtils.HttpRequestUtils.loadFileAsMultiPart(image)
        httpResponse = self.service.post(uri, requestBody, imageType==ImageType.FILE)
        return HttpUtils.HttpResponseUtils.httpResponse2Result(DetectFaceResult, httpResponse)

    def detectFaceByBase64(self, imageBase64, attributes=None):
        """
        Detect face by base64
        :rtype: DetectFaceResult
        """
        return self._detectFace(imageBase64, ImageType.BASE64, attributes)

    def detectFaceByObsUrl(self, obsUrl, attributes=None):
        """
        Detect face by obs url
        :rtype: DetectFaceResult
        """
        return self._detectFace(obsUrl, ImageType.OBSURL, attributes)

    def detectFaceByFile(self, filePath, attributes=None):
        """
        Detect face by file
        :rtype: DetectFaceResult
        """
        return self._detectFace(filePath, ImageType.FILE, attributes)