# _*_ coding: utf-8 _*_

from param import AuthInfo
from service import CompareService
from service import DetectService
from service import FaceService
from service import FaceSetService
from service import LiveDetectService
from service import SearchService
from access import FrsAccess
from common import FrsConstant

class FrsClient(object):
    """Create frs client

    service:
        detect service
        compare service
        face service
        face set service
        live detect service
        search service

    """
    
    def __init__(self, authInfo, projectId, proxyHostInfo=None,
                connectionTimeout=None, connectionRequestTimeout=None, socketTimeout=None):
        """
        :param projectId: Project ID
        :param authInfo: includes ak, sk, endPoint region
        :type authInfo: AuthInfo
        """

        self.service = FrsAccess(authInfo, connectionTimeout, connectionRequestTimeout, socketTimeout, proxyHostInfo)
        self.projectId = projectId

        self.detectService = DetectService(self.service, self.projectId)
        self.compareService = CompareService(self.service, self.projectId)
        self.liveDetectService = LiveDetectService(self.service, self.projectId)
        self.searchService = SearchService(self.service, self.projectId)
        self.faceSetService = FaceSetService(self.service, self.projectId)
        self.faceService = FaceService(self.service, self.projectId)


    def getDetectService(self):
        """
        Get detect service
        :rtype: DetectService
        """
        return self.detectService

    def getCompareService(self):
        """
        Get campare service
        :rtype: CompareService
        """
        return self.compareService
    
    def getLiveDetectService(self):
        """
        Get live detect service
        :rtype: LiveDetectService
        """
        return self.liveDetectService

    def getSearchService(self):
        """
        Get search service
        :rtype: SearchService
        """
        return self.searchService

    def getFaceSetService(self):
        """
        Get face set service
        :rtype: FaceSetService
        """
        return self.faceSetService

    def getFaceService(self):
        """
        Get face service
        :rtype: FaceService
        """
        return self.faceService
