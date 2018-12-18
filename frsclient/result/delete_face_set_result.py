# -*- coding: utf-8 -*-

class DeleteFaceSetResult(object):
    """Result of delete face set."""
    
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
    
    def get_face_set_name(self):
        """Get face_set_name.
        :rtype: str
        """
        return self.content_eval.get("face_set_name")