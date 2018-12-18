# -*- coding: utf-8 -*-

class LiveDetectResult(object):
    """Result of live detect."""
    
    def __init__(self, content):
        self.content_origin = content
        self.content_eval = eval(content.replace("true", "True").replace("false", "False"))

    def get_original_result(self):
        """Get original http content.
        :return: http content
        :rtype: str
        """
        return self.content_origin

    def get_eval_result(self):
        """Get Eval http content.
        :return: formatted http content, which is easy to use.
        :rtype: dict
        """
        return self.content_eval

    def get_video_result(self):
        """Get video result
        :rtype: dict
        """
        return self.content_eval.get("video-result")

    def get_warning_list(self):
        """Get warning list
        :rtype: list
        """
        return self.content_eval.get("warning-list")

    def get_alive(self):
        """Get alive
        :rtype: bool
        """
        return self.content_eval.get("video-result").get("alive")

    def get_picture(self):
        """Get face picture
        :rtype: str
        """
        return self.content_eval.get("video-result").get("picture")

    def get_actions(self):
        """Get actions
        :rtype: list
        """
        return self.content_eval.get("video-result").get("actions")