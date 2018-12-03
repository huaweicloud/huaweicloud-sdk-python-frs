# _*_ coding: utf-8 _*_

from utils import HttpUtils
from common import ImageType
from common import FrsConstant
from ..result import CompareFaceResult

class CompareService(object):

    def __init__(self, service, projectId):
        """Init
        :param service:
        :type service: FrsAccess
        """
        self.service = service
        self.projectId = projectId

    def _compareFace(self, image1, image2, imageType):
        """
        :rtype: CompareFaceResult
        """
        uri = FrsConstant.faceCompareUri % self.projectId
        requestBody = {}
        if imageType == ImageType.BASE64:
            if type(image1) is bytes:
                image1 = image1.decode()
            if type(image2) is bytes:
                image2 = image2.decode()
            requestBody["image1_base64"] = image1
            requestBody["image2_base64"] = image2
        elif imageType == ImageType.OBSURL:
            requestBody["image1_url"] = image1
            requestBody["image2_url"] = image2
        elif imageType == ImageType.FILE:
            requestBody['image1_file'] = HttpUtils.HttpRequestUtils.loadFileAsMultiPart(image1)
            requestBody['image2_file'] = HttpUtils.HttpRequestUtils.loadFileAsMultiPart(image2)
        httpResponse = self.service.post(uri, requestBody, imageType == ImageType.FILE)
        compareFaceResult = HttpUtils.HttpResponseUtils.httpResponse2Result(CompareFaceResult, httpResponse)
        return compareFaceResult

    def compareFaceByBase64(self, image1Base64, image2Base64):
        """
        Compare face by base64
        :rtype: CompareFaceResult
        """
        return self._compareFace(image1Base64, image2Base64, ImageType.BASE64)

    def compareFaceByObsUrl(self, obsUrl1, obsUrl2):
        """
        Compare face by obs url
        :rtype: CompareFaceResult
        """
        return self._compareFace(obsUrl1, obsUrl2, ImageType.OBSURL)

    def compareFaceByFile(self, filePath1, filePath2):
        """
        Compare face by file
        :rtype: CompareFaceResult
        """
        return self._compareFace(filePath1, filePath2, ImageType.FILE)

            
            