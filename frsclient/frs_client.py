# -*- coding: utf-8 -*-

from frsaccess import *
from frscommon import *
from frsclient.param import *
from frsclient.result import *
from frsclient.service import *


class FrsClient(object):
    """
    Creates a FRS(Face Recognize Service) frsclient with Initializing account information.

    Service kinds:
        Service Query   (Service Query API)
        Detect Service  (Detect API)
        Compare Service (Compare API)
        Face Service    (Face Resource API)
        Face Set Service(Face Set Resource API)
        Search Service  (Search API)
        Live Detect Service (Live Detect API)

    """

    def __init__(self, project_id=None, auth_info=None, ak=None, sk=None, proxies=None,
                 end_point=FrsConstant.END_POINT, region=FrsConstant.REGION,
                 connection_timeout=None, connection_request_timeout=None, socket_time_out=None):
        """
        Initial account information

        :param project_id:  Project ID
        :param auth_info:   Contains AK, SK, end_point, Region. (Choose one between auth_info and (ak, sk))
        :param ak:  Access Key ID.
        :param sk:  Secret Access Key.
        :param proxies: [Optional] Proxy info.
        :param end_point: [Optional] FRS address.
        :param region:    [Optional] Service area.
        :param connection_timeout:  [Optional] Requests connect timeout(unit:s).
        :param connection_request_timeout: [Optional] Requests read timeout(unit:s).
        :param socket_time_out:     [Optional] Scoket timeout(unit:s).
        """
        _auth_info = auth_info or AuthInfo(ak, sk, end_point, region)
        self.service = FrsAccess(_auth_info, connection_timeout, connection_request_timeout, socket_time_out, proxies)
        self.project_id = project_id
        self._apiCollectionV2 = ApiCollectionV2(self.service, self.project_id)

    def get_service_query(self):
        """Instantiates an object of 'ServiceQueryService' class.
        :rtype: ServiceQueryService
        """
        service_query_service = ServiceQueryService(self.service, self.project_id)
        return service_query_service

    def get_detect_service(self):
        """Instantiates an object of 'DetectService' class.
        :rtype: DetectService
        """
        detect_service = DetectService(self.service, self.project_id)
        return detect_service

    def get_compare_service(self):
        """Instantiates an object of 'CompareService' class.
        :rtype: CompareService
        """
        compare_service = CompareService(self.service, self.project_id)
        return compare_service
    
    def get_live_detect_service(self):
        """Instantiates an object of 'LiveDetectService' class.
        :rtype: LiveDetectService
        """
        live_detect_service = LiveDetectService(self.service, self.project_id)
        return live_detect_service

    def get_search_service(self):
        """Instantiates an object of 'SearchService' class.
        :rtype: SearchService
        """
        search_service = SearchService(self.service, self.project_id)
        return search_service

    def get_face_set_service(self):
        """Instantiates an object of 'FaceSetService' class.
        :rtype: FaceSetService
        """
        faceset_service = FaceSetService(self.service, self.project_id)
        return faceset_service

    def get_face_service(self):
        """Instantiates an object of 'FaceService' class.
        :rtype: FaceService
        """
        face_service = FaceService(self.service, self.project_id)
        return face_service

    def get_v2(self):
        """
        :rtype: ApiCollectionV2
        """
        return self._apiCollectionV2
