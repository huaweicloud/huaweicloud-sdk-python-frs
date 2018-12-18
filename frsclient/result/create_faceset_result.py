# -*- coding: utf-8 -*-

class CreateFaceSetResult(object):
    """Result of create face set."""
    
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

    def get_face_set_info(self):
        """Get Face set info
        :rtype: dict
        """
        return self.content_eval.get("face_set_info")

    def get_create_date(self):
        """Get create_date
        :rtype: str 
        """
        return self.content_eval.get("face_set_info").get("create_date")

    def get_face_set_capacity(self):
        """Get face_set_capacity
        :rtype: int 
        """
        return self.content_eval.get("face_set_info").get("face_set_capacity")

    def get_face_set_id(self):
        """Get face_set_id
        :rtype: str
        """
        return self.content_eval.get("face_set_info").get("face_set_id")

    def get_face_number(self):
        """Get face_number
        :rtype: int
        """
        return self.content_eval.get("face_set_info").get("face_number")

    def get_external_fields(self):
        """Get external_fields
        :rtype: str
        """
        return self.content_eval.get("face_set_info").get("external_fields")

    def get_face_set_name(self):
        """Get face_set_name
        :rtype: str
        """
        return self.content_eval.get("face_set_info").get("face_set_name")