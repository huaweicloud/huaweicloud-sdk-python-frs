# -*- coding: utf-8 -*-

class ServiceQueryResult(object):
    """Result of service query."""

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

    def get_max_face_set_number(self):
        """Get max set number
        :rtype: int
        """
        return self.content_eval.get("max_face_set_number")

    def get_detect_service(self):
        """Get detect service
        :return: Service info
        """
        return self.content_eval.get("detect_service")

    def get_compare_service(self):
        """Get compare service
        :return: Service info
        """
        return self.content_eval.get("compare_service")

    def get_live_detect_service(self):
        """Get live detect service
        :return: Service info
        """
        return self.content_eval.get("live_detect_service")

    def get_search_service(self):
        """Get search service
        :return: Service info
        """
        return self.content_eval.get("search_service")