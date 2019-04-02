# -*- coding: utf-8 -*-

from frsaccess import FrsAccess
from frscommon import FrsConstantV2
from frscommon import VideoType
from frsutils import http_utils
from frsclient.result import LiveDetectResult


class LiveDetectServiceV2(object):

    def __init__(self, service, project_id):
        """Initializes the service
        :type service: FrsAccess
        """
        self.service = service
        self.project_id = project_id

    def _live_detect(self, video, video_type, actions, action_time):
        """
        :rtype: LiveDetectResult
        """
        uri = FrsConstantV2.LIVE_DETECT_URI % self.project_id
        request_body = {}
        if actions:
            request_body["actions"] = actions
        if action_time:
            request_body["action_time"] = action_time
        if video_type == VideoType.BASE64:
            if type(video) is bytes:
                request_body['video_base64'] = video.decode()
            else:
                request_body['video_base64'] = video
        elif video_type == VideoType.OBSURL:
            request_body['video_url'] = video
        elif video_type == VideoType.FILE:
            request_body['video_file'] = http_utils.HttpRequestUtils.load_file_as_multi_part(video)
        http_response = self.service.post(uri, request_body, video_type == VideoType.FILE)
        return http_utils.HttpResponseUtils.http_response2_result(LiveDetectResult, http_response)

    def live_detect_by_base64(self, video_base64, actions=None, action_time=None):
        """
        Live detect by base64
        :rtype: LiveDetectResult
        """
        return self._live_detect(video_base64, VideoType.BASE64, actions, action_time)

    def live_detect_by_obsurl(self, video_url, actions=None, action_time=None):
        """
        Live detect by obs url
        :rtype: LiveDetectResult
        """
        return self._live_detect(video_url, VideoType.OBSURL, actions, action_time)

    def live_detect_by_file(self, video_file, actions=None, action_time=None):
        """
        Live detect by file
        :rtype: LiveDetectResult
        """
        return self._live_detect(video_file, VideoType.FILE, actions, action_time)