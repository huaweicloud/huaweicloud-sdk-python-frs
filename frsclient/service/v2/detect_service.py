# -*- coding: utf-8 -*-

from frsaccess import FrsAccess
from frscommon import FrsConstantV2
from frscommon import ImageType
from frsutils import http_utils
from frsclient.result import DetectFaceResult


class DetectServiceV2(object):

    def __init__(self, service, project_id):
        """Initializes the service
        :type service: FrsAccess
        """
        self.service = service
        self.project_id = project_id

    def _detect_face(self, image, image_type, attributes):
        """
        :rtype: DetectFaceResult
        """
        uri = FrsConstantV2.FACE_DETECT_URI % self.project_id
        request_body = {}
        if attributes:
            request_body['attributes'] = attributes
        if image_type == ImageType.BASE64:
            if type(image) is bytes:
                request_body['image_base64'] = image.decode()
            else:
                request_body['image_base64'] = image
        elif image_type == ImageType.OBSURL:
            request_body['image_url'] = image
        elif image_type == ImageType.FILE:
            request_body['image_file'] = http_utils.HttpRequestUtils.load_file_as_multi_part(image)
        http_response = self.service.post(uri, request_body, image_type == ImageType.FILE)
        return http_utils.HttpResponseUtils.http_response2_result(DetectFaceResult, http_response)

    def detect_face_by_base64(self, image_base64):
        """
        Detect face by base64
        :rtype: DetectFaceResult
        """
        return self._detect_face(image_base64, ImageType.BASE64, None)

    def detect_face_by_obsurl(self, obsurl):
        """
        Detect face by obs url
        :rtype: DetectFaceResult
        """
        return self._detect_face(obsurl, ImageType.OBSURL, None)

    def detect_face_by_file(self, file_path):
        """
        Detect face by file
        :rtype: DetectFaceResult
        """
        return self._detect_face(file_path, ImageType.FILE, None)