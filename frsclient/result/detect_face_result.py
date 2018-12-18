# -*- coding: utf-8 -*-

class DetectFaceResult(object):
    """Result of detect face."""
    
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
    
    def get_faces(self):
        """Get faces
        :rtype: list
        """
        return self.content_eval.get("faces")

    def get_bounding_box(self, face_index=0):
        """Get bounding box
        :rtype: dict
        """
        return self.content_eval.get("faces")[face_index].get("bounding_box")