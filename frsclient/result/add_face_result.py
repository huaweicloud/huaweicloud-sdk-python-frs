# -*- coding: utf-8 -*-

class AddFaceResult(object):
    """Result of add face"""

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

    def get_face_set_id(self):
        """Get face_set_id
        :rtype: str
        """
        return self.content_eval.get("face_set_id")

    def get_faces(self):
        """Get faces
        :rtype: list
        """
        return self.content_eval.get("faces")

    def get_face_id(self, face_index=0):
        """Get face_id of nth face.
        :rtype: str
        """
        return self.content_eval.get("faces")[face_index].get("face_id")

    def get_external_fields(self, face_index=0):
        """Get external fields of nth face.
        :rtype: str
        """
        return self.content_eval.get("faces")[face_index].get("external_fields")

    def get_bounding_box(self, face_index=0):
        """Get bounding_box of nth face.
        :rtype: dict
        """
        return self.content_eval.get("faces")[face_index].get("bounding_box")