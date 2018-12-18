# -*- coding: utf-8 -*-

from access import FrsAccess
from common import FrsConstant
from utils import http_utils
from frsclient.result import CreateFaceSetResult
from frsclient.result import GetAllFaceSetsResult
from frsclient.result import GetFaceSetResult
from frsclient.result import DeleteFaceSetResult

class FaceSetService(object):

    def __init__(self, service, project_id):
        """Initializes the service
        :type service: FrsAccess
        """
        self.service = service
        self.projectId = project_id

    def create_face_set(self, face_set_name, face_set_capacity=None, external_fields=None):
        """
        :rtype: CreateFaceSetResult
        """
        uri = FrsConstant.FACE_SET_CREATE_URI % self.projectId
        request_body = {}
        request_body['face_set_name'] = face_set_name
        if face_set_capacity:
            request_body['face_set_capacity'] = face_set_capacity
        if external_fields:
            request_body['external_fields'] = external_fields
        httpResponse = self.service.post(uri, request_body)
        return http_utils.HttpResponseUtils.httpResponse2Result(CreateFaceSetResult, httpResponse)

    def get_all_face_sets(self):
        """
        :rtype: GetAllFaceSetsResult
        """
        uri = FrsConstant.FACE_SET_GET_ALL_URI % self.projectId
        http_response = self.service.get(uri)
        return http_utils.HttpResponseUtils.httpResponse2Result(GetAllFaceSetsResult, http_response)

    def get_face_set(self, face_set_name):
        """
        :rtype: GetFaceSetResult
        """
        uri = FrsConstant.FACE_SET_GET_ONE_URI % (self.projectId, face_set_name)
        http_response = self.service.get(uri)
        return http_utils.HttpResponseUtils.httpResponse2Result(GetFaceSetResult, http_response)

    def delete_face_set(self, face_set_name):
        """
        :rtype: DeleteFaceSetResult
        """
        uri = FrsConstant.FACE_SET_DELETE_URI % (self.projectId, face_set_name)
        http_response = self.service.delete(uri)
        return http_utils.HttpResponseUtils.httpResponse2Result(DeleteFaceSetResult, http_response)
        