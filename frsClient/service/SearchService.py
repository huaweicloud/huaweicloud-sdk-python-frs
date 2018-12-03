# _*_ coding: utf-8 _*_

from utils import HttpUtils
from common import ImageType
from common import FrsConstant
from ..result import SearchFaceResult

class SearchService(object):

    def __init__(self, service, projectId):
        """Init
        :type service: FrsAccess
        """
        self.service = service
        self.projectId = projectId

    def _searchFace(self, faceSetName, image, imageType, topN, threshold, searchSort, searchReturnFields, filter):
        """
        :rtype: SearchFaceResult
        """
        uri = FrsConstant.faceSearchUri % (self.projectId, faceSetName)
        requestBody = {}
        if imageType == ImageType.BASE64:
            if type(image) is bytes:
                requestBody["image_base64"] = image.decode()
            else:
                requestBody["image_base64"] = image
        elif imageType == ImageType.OBSURL:
            requestBody['image_url'] = image
        elif imageType == ImageType.FILE:
            requestBody['image_file'] = HttpUtils.HttpRequestUtils.loadFileAsMultiPart(image)
        if topN:
            requestBody["top_n"] = topN
        if threshold:
            requestBody["threshold"] = threshold
        if searchSort:
            requestBody["sort"] = searchSort
        if searchReturnFields:
            requestBody["return_fields"] = searchReturnFields
        if filter:
            requestBody["filter"] = filter
        httpResponse = self.service.post(uri, requestBody, imageType==ImageType.FILE)
        return HttpUtils.HttpResponseUtils.httpResponse2Result(SearchFaceResult, httpResponse)
        
    def searchFaceByBase64(self, faceSetName, image, 
                            topN=None, threshold=None, searchSort=None, searchReturnFields=None, filter=None):
        """
        Search face by base64
        :rtype: SearchFaceResult
        """
        return self._searchFace(faceSetName, image, ImageType.BASE64, topN, threshold, searchSort, searchReturnFields, filter)

    def searchFaceByObsUrl(self, faceSetName, image,
                            topN=None, threshold=None, searchSort=None, searchReturnFields=None, filter=None):
        """
        Search face by obs url
        :rtype: SearchFaceResult
        """
        return self._searchFace(faceSetName, image, ImageType.OBSURL, topN, threshold, searchSort, searchReturnFields, filter)

    def searchFaceByFile(self, faceSetName, image,
                        topN=None, threshold=None, searchSort=None, searchReturnFields=None, filter=None):
        """
        Search face by file
        :rtype: SearchFaceResult
        """
        return self._searchFace(faceSetName, image, ImageType.FILE, topN, threshold, searchSort, searchReturnFields, filter)