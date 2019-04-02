# -*- coding: utf-8 -*-

from frsaccess import FrsAccess
from frscommon import FrsConstantV2
from frsutils import http_utils
from frsclient.result import CreateFaceSetResult
from frsclient.result import GetAllFaceSetsResult
from frsclient.result import GetFaceSetResult
from frsclient.result import DeleteFaceSetResult


class FaceSetServiceV2(object):

    def __init__(self, service, project_id):
        """Initializes the service
        :type service: FrsAccess
        """
        self.service = service
        self.project_id = project_id

    def create_face_set(self, face_set_name, face_set_capacity=None, external_fields=None):
        """
        :rtype: CreateFaceSetResult
        """
        uri = FrsConstantV2.FACE_SET_CREATE_URI % self.project_id
        request_body = {}
        request_body['face_set_name'] = face_set_name
        if face_set_capacity:
            request_body['face_set_capacity'] = face_set_capacity
        if external_fields:
            request_body['external_fields'] = external_fields
        httpResponse = self.service.post(uri, request_body)
        return http_utils.HttpResponseUtils.http_response2_result(CreateFaceSetResult, httpResponse)

    def get_all_face_sets(self):
        """
        :rtype: GetAllFaceSetsResult
        """
        uri = FrsConstantV2.FACE_SET_GET_ALL_URI % self.project_id
        http_response = self.service.get(uri)
        return http_utils.HttpResponseUtils.http_response2_result(GetAllFaceSetsResult, http_response)

    def get_face_set(self, face_set_name):
        """
        :rtype: GetFaceSetResult
        """
        uri = FrsConstantV2.FACE_SET_GET_ONE_URI % (self.project_id, face_set_name)
        http_response = self.service.get(uri)
        return http_utils.HttpResponseUtils.http_response2_result(GetFaceSetResult, http_response)

    def delete_face_set(self, face_set_name):
        """
        :rtype: DeleteFaceSetResult
        """
        uri = FrsConstantV2.FACE_SET_DELETE_URI % (self.project_id, face_set_name)
        http_response = self.service.delete(uri)
        return http_utils.HttpResponseUtils.http_response2_result(DeleteFaceSetResult, http_response)
