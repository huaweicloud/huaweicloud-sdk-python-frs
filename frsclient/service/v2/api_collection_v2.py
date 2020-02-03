# -*- coding: utf-8 -*-

from frsclient.service.v2.compare_service import CompareServiceV2
from frsclient.service.v2.detect_service import DetectServiceV2
from frsclient.service.v2.face_service import FaceServiceV2
from frsclient.service.v2.face_set_service import FaceSetServiceV2
from frsclient.service.v2.live_detect_service import LiveDetectServiceV2
from frsclient.service.v2.search_service import SearchServiceV2


class ApiCollectionV2(object):
    """
    v2 api collection
    """
    def __init__(self, service, project_id):
        self._compare_service = CompareServiceV2(service, project_id)
        self._detect_service = DetectServiceV2(service, project_id)
        self._face_service = FaceServiceV2(service, project_id)
        self._face_set_service = FaceSetServiceV2(service, project_id)
        self._live_detect_service = LiveDetectServiceV2(service, project_id)
        self._search_service = SearchServiceV2(service, project_id)

    def get_detect_service(self):
        """Instantiates an object of 'DetectService' class.
        :rtype: DetectServiceV2
        """
        return self._detect_service

    def get_compare_service(self):
        """Instantiates an object of 'CompareService' class.
        :rtype: CompareServiceV2
        """
        return self._compare_service

    def get_live_detect_service(self):
        """Instantiates an object of 'LiveDetectService' class.
        :rtype: LiveDetectServiceV2
        """
        return self._live_detect_service

    def get_search_service(self):
        """Instantiates an object of 'SearchService' class.
        :rtype: SearchServiceV2
        """
        return self._search_service

    def get_face_set_service(self):
        """Instantiates an object of 'FaceSetService' class.
        :rtype: FaceSetServiceV2
        """
        return self._face_set_service

    def get_face_service(self):
        """Instantiates an object of 'FaceService' class.
        :rtype: FaceServiceV2
        """
        return self._face_service
