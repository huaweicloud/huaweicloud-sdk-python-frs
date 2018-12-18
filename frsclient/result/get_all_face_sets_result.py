# -*- coding: utf-8 -*-

class GetAllFaceSetsResult(object):
    """Result of get all face sets."""
    
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

    def get_face_sets_info(self):
        """Get face_sets_info
        :rtype: dict
        """
        return self.content_eval.get("face_sets_info")

    def get_create_date(self, face_set_index=0):
        """Get create_date
        :rtype: str
        """
        return self.content_eval.get("face_sets_info")[face_set_index].get("create_date")

    def get_face_set_capacity(self, face_set_index=0):
        """Get capacity
        :rtype: int
        """
        return self.content_eval.get("face_sets_info")[face_set_index].get("face_set_capacity")

    def get_face_set_id(self, face_set_index=0):
        """Get face_set_id
        :rtype: str
        """
        return self.content_eval.get("face_sets_info")[face_set_index].get("face_set_id")

    def get_face_number(self, face_set_index=0):
        """Get face_number
        :rtype: int
        """
        return self.content_eval.get("face_sets_info")[face_set_index].get("face_number")

    def get_external_fields(self, face_set_index=0):
        """Get face_number
        :rtype: str
        """
        return self.content_eval.get("face_sets_info")[face_set_index].get("external_fields")

    def get_face_set_name(self, face_set_index=0):
        """Get face_set_name
        :rtype: str
        """
        return self.content_eval.get("face_sets_info")[face_set_index].get("face_set_name")

    def get_face_sets_number(self):
        """Get face sets number
        :rtype: int
        """
        return len(self.content_eval.get("face_sets_info"))