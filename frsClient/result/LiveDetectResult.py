# _*_ coding: utf-8 _*_

class LiveDetectResult(object):
    """Result of live detect."""
    
    def __init__(self, content):
        self.contentOrigin = content
        self.contentEval = eval(content.replace("true", "True").replace("false", "False"))

    def getOriginalResult(self):
        """Get original http content.
        :return: http content
        :rtype: str
        """
        return self.contentOrigin

    def getEvalResult(self):
        """Get Eval http content.
        :return: formatted http content, which is easy to use.
        :rtype: dict
        """
        return self.contentEval

    def getVideoResult(self):
        """Get video result
        :rtype: dict
        """
        return self.contentEval.get("video-result")

    def getWarningList(self):
        """Get warning list
        :rtype: list
        """
        return self.contentEval.get("warning-list")

    def getAliveResult(self):
        """Get alive
        :rtype: bool
        """
        return self.contentEval.get("video-result").get("alive")

    def getPictureResult(self):
        """Get face picture
        :rtype: str
        """
        return self.contentEval.get("video-result").get("picture")

    def getActions(self):
        """Get actions
        :rtype: list
        """
        return self.contentEval.get("video-result").get("actions")