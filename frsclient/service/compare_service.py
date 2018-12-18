# -*- coding: utf-8 -*-

from frsaccess import FrsAccess
from frscommon import FrsConstant
from frscommon import ImageType
from frsutils import http_utils
from frsclient.result import CompareFaceResult


class CompareService(object):

    def __init__(self, service, project_id):
        """Initializes the service
        :type service: FrsAccess
        """
        self.service = service
        self.project_id = project_id

    def _compare_face(self, image1, image2, image_type):
        """
        :rtype: CompareFaceResult
        """
        uri = FrsConstant.FACE_COMPARE_URI % self.project_id
        request_body = {}
        if image_type == ImageType.BASE64:
            if type(image1) is bytes:
                image1 = image1.decode()
            if type(image2) is bytes:
                image2 = image2.decode()
            request_body["image1_base64"] = image1
            request_body["image2_base64"] = image2
        elif image_type == ImageType.OBSURL:
            request_body["image1_url"] = image1
            request_body["image2_url"] = image2
        elif image_type == ImageType.FILE:
            request_body['image1_file'] = http_utils.HttpRequestUtils.load_file_as_multi_part(image1)
            request_body['image2_file'] = http_utils.HttpRequestUtils.load_file_as_multi_part(image2)
        http_response = self.service.post(uri, request_body, image_type == ImageType.FILE)
        compare_face_result = http_utils.HttpResponseUtils.http_response2_result(CompareFaceResult, http_response)
        return compare_face_result

    def compare_face_by_base64(self, image1_base64, image2_base64):
        """
        Compare face by base64
        :rtype: CompareFaceResult
        """
        return self._compare_face(image1_base64, image2_base64, ImageType.BASE64)

    def compare_face_by_obsurl(self, obsurl1, obsurl2):
        """
        Compare face by obs url
        :rtype: CompareFaceResult
        """
        return self._compare_face(obsurl1, obsurl2, ImageType.OBSURL)

    def compare_face_by_file(self, file_path1, file_path2):
        """
        Compare face by file
        :rtype: CompareFaceResult
        """
        return self._compare_face(file_path1, file_path2, ImageType.FILE)

            
            