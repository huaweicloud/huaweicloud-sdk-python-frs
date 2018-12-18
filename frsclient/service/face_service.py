# -*- coding: utf-8 -*-

from frsaccess import FrsAccess
from frscommon import FrsConstant
from frscommon import ImageType
from frsutils import http_utils
from frsclient.result import AddFaceResult
from frsclient.result import GetFaceResult
from frsclient.result import DeleteFaceResult


class FaceService(object):

    def __init__(self, service, project_id):
        """Initializes the service
        :type service: FrsAccess
        """
        self.service = service
        self.project_id = project_id

    def _add_face(self, face_set_name, image, image_type, external_image_id, external_fields):
        """
        :rtype: AddFaceResult
        """
        uri = FrsConstant.FACE_ADD_URI % (self.project_id, face_set_name)
        request_body = {}
        if image_type == ImageType.BASE64:
            if type(image) is bytes:
                request_body['image_base64'] = image.decode()
            else:
                request_body['image_base64'] = image
        elif image_type == ImageType.OBSURL:
            request_body['image_url'] = image
        elif image_type == ImageType.FILE:
            request_body['image_file'] = http_utils.HttpRequestUtils.load_file_as_multi_part(image)
        if external_image_id:
            request_body['external_image_id'] = external_image_id
        if external_fields:
            request_body['external_fields'] = external_fields
        http_response = self.service.post(uri, request_body, image_type == ImageType.FILE)
        return http_utils.HttpResponseUtils.http_response2_result(AddFaceResult, http_response)

    def add_face_by_base64(self, face_set_name, image, external_image_id=None, external_fields=None):
        """
        Add face by base64
        :rtype: AddFaceResult
        """
        return self._add_face(face_set_name, image, ImageType.BASE64, external_image_id, external_fields)

    def add_face_by_file(self, face_set_name, image, external_image_id=None, external_fields=None):
        """
        Add face by file
        :rtype: AddFaceResult
        """
        return self._add_face(face_set_name, image, ImageType.FILE, external_image_id, external_fields)

    def add_face_by_obsurl(self, face_set_name, image, external_image_id=None, external_fields=None):
        """
        Add face by obs url
        :rtype: AddFaceResult
        """
        return self._add_face(face_set_name, image, ImageType.OBSURL, external_image_id, external_fields)
    
    def _get_face(self, face_set_name, offset=None, limit=None, face_id=None):
        """
        :rtype: GetFaceResult
        """
        if face_id:
            uri = FrsConstant.FACE_GET_ONE_URI % (self.project_id, face_set_name, face_id)
        elif offset or limit:
            uri = FrsConstant.FACE_GET_RANGE_URI % (self.project_id, face_set_name, offset, limit)
        else:
            uri = FrsConstant.FACE_GET_BASE_URI % (self.project_id, face_set_name)
        http_response = self.service.get(uri)
        return http_utils.HttpResponseUtils.http_response2_result(GetFaceResult, http_response)

    def get_face(self, face_set_name, face_id):
        """
        Get face by face id
        :rtype: GetFaceResult
        """
        return self._get_face(face_set_name, face_id=face_id)

    def get_faces(self, face_set_name, offset=0, limit=5):
        """
        Get faces by range
        :rtype: GetFaceResult
        """
        return self._get_face(face_set_name, offset=offset, limit=limit)

    def _delete_face(self, face_set_name, external_image_id=None, face_id=None, field_id=None, field_value=None):
        """
        :rtype: DeleteFaceResult
        """
        if external_image_id:
            uri = FrsConstant.FACE_DELETE_BY_EXTERNAL_IMAGE_ID_URI % (self.project_id, face_set_name, external_image_id)
        elif face_id:
            uri = FrsConstant.FACE_DELETE_BY_FACE_ID_URI % (self.project_id, face_set_name, face_id)
        else:
            uri = FrsConstant.FACE_DELETE_BY_FIELD_ID_URI % (self.project_id, face_set_name, field_id, field_value)
        http_response = self.service.delete(uri)
        return http_utils.HttpResponseUtils.http_response2_result(DeleteFaceResult, http_response)

    def delete_face_by_external_image_id(self, face_set_name, external_image_id):
        """
        Delete face by external image id
        :rtype: DeleteFaceResult
        """
        return self._delete_face(face_set_name, external_image_id=external_image_id)

    def delete_face_by_face_id(self, face_set_name, face_id):
        """
        Delete face by face id
        :rtype: DeleteFaceResult
        """
        return self._delete_face(face_set_name, face_id=face_id)

    def delete_face_by_field_id(self, face_set_name, field_id, field_value):
        """
        Delete face by field id
        :rtype: DeleteFaceResult
        """
        return self._delete_face(face_set_name, field_id=field_id, field_value=field_value)
