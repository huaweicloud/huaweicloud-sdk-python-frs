# _*_ coding: utf-8 _*_

from utils import HttpUtils
from common import FrsConstant
from common import ImageType
from ..result import CreateFaceSetResult
from ..result import GetAllFaceSetsResult
from ..result import GetFaceSetResult
from ..result import DeleteFaceSetResult

class FaceSetService(object):

    def __init__(self, service, projectId):
        """Init
        :param service:
        :type service: FrsAccess
        """
        self.service = service
        self.projectId = projectId

    def createFaceSet(self, faceSetName, faceSetCapacity=None, externalFields=None):
        """
        :rtype: CreateFaceSetResult
        """
        uri = FrsConstant.faceSetCreateUri % self.projectId
        requestBody = {}
        requestBody['face_set_name'] = faceSetName
        if faceSetCapacity:
            requestBody['face_set_capacity'] = faceSetCapacity
        if externalFields:
            requestBody['external_fields'] = externalFields
        httpResponse = self.service.post(uri, requestBody)
        return HttpUtils.HttpResponseUtils.httpResponse2Result(CreateFaceSetResult, httpResponse)

    def getAllFaceSets(self):
        """
        :rtype: GetAllFaceSetsResult
        """
        uri = FrsConstant.faceSetGetAllUri % self.projectId
        httpResponse = self.service.get(uri)
        return HttpUtils.HttpResponseUtils.httpResponse2Result(GetAllFaceSetsResult, httpResponse)

    def getFaceSet(self, faceSetName):
        """
        :rtype: GetFaceSetResult
        """
        uri = FrsConstant.faceSetGetOneUri % (self.projectId, faceSetName)
        httpResponse = self.service.get(uri)
        return HttpUtils.HttpResponseUtils.httpResponse2Result(GetFaceSetResult, httpResponse)

    def deleteFaceSet(self, faceSetName):
        """
        :rtype: DeleteFaceSetResult
        """
        uri = FrsConstant.faceSetDeleteUri % (self.projectId, faceSetName)
        httpResponse = self.service.delete(uri)
        return HttpUtils.HttpResponseUtils.httpResponse2Result(DeleteFaceSetResult, httpResponse)
        