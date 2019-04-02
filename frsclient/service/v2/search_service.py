# -*- coding: utf-8 -*-

from frsaccess import FrsAccess
from frscommon import FrsConstantV2
from frscommon import ImageType
from frsutils import http_utils
from frsclient.result import SearchFaceResult


class SearchServiceV2(object):

    def __init__(self, service, project_id):
        """Initializes the service
        :type service: FrsAccess
        """
        self.service = service
        self.project_id = project_id

    def _search_face(self, face_set_name, image, image_type, top_n, threshold, search_sort, search_return_fields, filter):
        """
        :rtype: SearchFaceResult
        """
        uri = FrsConstantV2.FACE_SEARCH_URI % (self.project_id, face_set_name)
        request_body = {}
        if image_type == ImageType.BASE64:
            if type(image) is bytes:
                request_body["image_base64"] = image.decode()
            else:
                request_body["image_base64"] = image
        elif image_type == ImageType.OBSURL:
            request_body['image_url'] = image
        elif image_type == ImageType.FILE:
            request_body['image_file'] = http_utils.HttpRequestUtils.load_file_as_multi_part(image)
        if top_n:
            request_body["top_n"] = top_n
        if threshold:
            request_body["threshold"] = threshold
        if search_sort:
            request_body["sort"] = search_sort
        if search_return_fields:
            request_body["return_fields"] = search_return_fields
        if filter:
            request_body["filter"] = filter
        http_response = self.service.post(uri, request_body, image_type == ImageType.FILE)
        return http_utils.HttpResponseUtils.http_response2_result(SearchFaceResult, http_response)
        
    def search_face_by_base64(self, face_set_name, image, top_n=None, threshold=None,
                              search_sort=None, search_return_fields=None, filter=None):
        """
        Search face by base64
        :rtype: SearchFaceResult
        """
        return self._search_face(face_set_name, image, ImageType.BASE64, top_n, threshold, search_sort, search_return_fields, filter)

    def search_face_by_obsurl(self, face_set_name, image, top_n=None, threshold=None,
                              search_sort=None, search_return_fields=None, filter=None):
        """
        Search face by obs url
        :rtype: SearchFaceResult
        """
        return self._search_face(face_set_name, image, ImageType.OBSURL, top_n, threshold, search_sort, search_return_fields, filter)

    def search_face_by_file(self, face_set_name, image, top_n=None, threshold=None,
                            search_sort=None, search_return_fields=None, filter=None):
        """
        Search face by file
        :rtype: SearchFaceResult
        """
        return self._search_face(face_set_name, image, ImageType.FILE, top_n, threshold, search_sort, search_return_fields, filter)