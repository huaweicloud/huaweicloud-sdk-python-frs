# -*- coding: utf-8 -*-

from access import FrsAccess
from common import FrsConstant
from utils import http_utils
from frsclient.result import ServiceQueryResult


class ServiceQueryService(object):

    def __init__(self, service, project_id):
        """Initializes the service
        :type service: FrsAccess
        """
        self.service = service
        self.project_id = project_id

    def _service_query(self):
        """
        :rtype: ServiceQueryResult
        """
        uri = FrsConstant.SERVICE_QUERY_URI % self.project_id
        http_response = self.service.get(uri)
        service_query_result = http_utils.HttpResponseUtils.httpResponse2Result(ServiceQueryService, http_response)
        return service_query_result

    def service_query(self):
        """
        :rtype: ServiceQueryResult
        """
        return self._service_query()