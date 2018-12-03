# _*_ coding: utf-8 _*_

from utils import HttpUtils
from common import FrsConstant
from common import ImageType
from ..result import AddFaceResult
from ..result import GetFaceResult
from ..result import DeleteFaceResult

class FaceService(object):

    def __init__(self, service, projectId):
        """Init
        :param service:
        :type service: FrsAccess
        """
        self.service = service
        self.projectId = projectId

    def _addFace(self, faceSetName, image, imageType, externalImageId, externalFields):
        """
        :rtype: AddFaceResult
        """
        uri = FrsConstant.faceAddUri % (self.projectId, faceSetName)
        requestBody = {}
        if imageType == ImageType.BASE64:
            if type(image) is bytes:
                requestBody['image_base64'] = image.decode()
            else:
                requestBody['image_base64'] = image
        elif imageType == ImageType.OBSURL:
            requestBody['image_url'] = image
        elif imageType == ImageType.FILE:
            requestBody['image_file'] = HttpUtils.HttpRequestUtils.loadFileAsMultiPart(image)
        if externalImageId:
            requestBody['external_image_id'] = externalImageId
        if externalFields:
            requestBody['external_fields'] = externalFields
        httpResponse = self.service.post(uri, requestBody, imageType==ImageType.FILE)
        return HttpUtils.HttpResponseUtils.httpResponse2Result(AddFaceResult, httpResponse)

    def addFaceByBase64(self, faceSetName, image, externalImageId=None, externalFields=None):
        """
        Add face by base64
        :rtype: AddFaceResult
        """
        return self._addFace(faceSetName, image, ImageType.BASE64, externalImageId, externalFields)

    def addFaceByFile(self, faceSetName, image, externalImageId=None, externalFields=None):
        """
        Add face by file
        :rtype: AddFaceResult
        """
        return self._addFace(faceSetName, image, ImageType.FILE, externalImageId, externalFields)

    def addFaceByObsUrl(self, faceSetName, image, externalImageId=None, externalFields=None):
        """
        Add face by obs url
        :rtype: AddFaceResult
        """
        return self._addFace(faceSetName, image, ImageType.OBSURL, externalImageId, externalFields)
    
    def _getFace(self, faceSetName, offset=None, limit=None, faceId=None):
        """
        :rtype: GetFaceResult
        """
        if faceId:
            uri = FrsConstant.faceGetOneUri % (self.projectId, faceSetName, faceId)
        elif offset or limit:
            uri = FrsConstant.faceGetRangeUri % (self.projectId, faceSetName, offset, limit)
        else:
            uri = FrsConstant.faceGetBaseUri % (self.projectId, faceSetName)
        httpResponse = self.service.get(uri)
        return HttpUtils.HttpResponseUtils.httpResponse2Result(GetFaceResult, httpResponse)

    def getFace(self, faceSetName, faceId):
        """
        Get face by face id
        :rtype: GetFaceResult
        """
        return self._getFace(faceSetName, faceId=faceId)

    def getFaces(self, faceSetName, offset=0, limit=5):
        """
        Get faces by range
        :rtype: GetFaceResult
        """
        return self._getFace(faceSetName, offset=offset, limit=limit)

    def _deleteFace(self, faceSetName, externalImageId=None, faceId=None, fieldId=None, fieldValue=None):
        """
        :rtype: DeleteFaceResult
        """
        if externalImageId:
            uri = FrsConstant.faceDeleteByExternalImageIdUri % (self.projectId, faceSetName, externalImageId)
        elif faceId:
            uri = FrsConstant.faceDeleteByFaceIdUri % (self.projectId, faceSetName, faceId)
        else:
            uri = FrsConstant.faceDeleteByFieldIdUri % (self.projectId, faceSetName, fieldId, fieldValue)
        httpResponse = self.service.delete(uri)
        return HttpUtils.HttpResponseUtils.httpResponse2Result(DeleteFaceResult, httpResponse)

    def deleteFaceByExternalImageId(self, faceSetName, externalImageId):
        """
        Delete face by external image id
        :rtype: DeleteFaceResult
        """
        return self._deleteFace(faceSetName, externalImageId=externalImageId)

    def deleteFaceByFaceId(self, faceSetName, faceId):
        """
        Delete face by face id
        :rtype: DeleteFaceResult
        """
        return self._deleteFace(faceSetName, faceId=faceId)

    def deleteFaceByFieldId(self, faceSetName, fieldId, fieldValue):
        """
        Delete face by field id
        :rtype: DeleteFaceResult
        """
        return self._deleteFace(faceSetName, fieldId=fieldId, fieldValue=fieldValue)
