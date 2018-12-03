# _*_ coding: utf-8 _*_

from utils import HttpUtils
from common import VideoType
from common import FrsConstant
from ..result import LiveDetectResult

class LiveDetectService(object):

    def __init__(self, service, projectId):
        """Init
        :param service:
        :type service: FrsAccess
        """
        self.service = service
        self.projectId = projectId

    def _liveDetect(self, video, videoType, actions, actionTime):
        """
        :rype: LiveDetectResult
        """
        uri = FrsConstant.liveDetectUri % self.projectId
        requestBody = {}
        if actions:
            requestBody["actions"] = actions
        if actionTime:
            requestBody["action_time"] = actionTime
        if videoType == VideoType.BASE64:
            if type(video) is bytes:
                requestBody['video_base64'] = video.decode()
            else:
                requestBody['video_base64'] = video
        elif videoType == VideoType.OBSURL:
            requestBody['video_url'] = video
        elif videoType == VideoType.FILE:
            requestBody['video_file'] = HttpUtils.HttpRequestUtils.loadFileAsMultiPart(video)
        httpResponse = self.service.post(uri, requestBody, videoType==VideoType.FILE)
        return HttpUtils.HttpResponseUtils.httpResponse2Result(LiveDetectResult, httpResponse)

    def liveDetectByBase64(self, videoBase64, actions=None, actionTime=None):
        """
        Live detect by base64
        :rype: LiveDetectResult
        """
        return self._liveDetect(videoBase64, VideoType.BASE64, actions, actionTime)

    def liveDetectByObsUrl(self, videoUrl, actions=None, actionTime=None):
        """
        Live detect by obs url
        :rype: LiveDetectResult
        """
        return self._liveDetect(videoUrl, VideoType.OBSURL, actions, actionTime)

    def liveDetectByFile(self, videoFile, actions=None, actionTime=None):
        """
        Live detect by file
        :rype: LiveDetectResult
        """
        return self._liveDetect(videoFile, VideoType.FILE, actions, actionTime)