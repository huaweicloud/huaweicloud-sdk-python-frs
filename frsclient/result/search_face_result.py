# -*- coding: utf-8 -*-

class SearchFaceResult(object):
    """Result of search face."""
    
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

    def get_external_image_id(self, face_sim_rank=0):
        """Get external_image_id
        :rtype: str
        """
        return self.content_eval.get("faces")[face_sim_rank].get("external_image_id")

    def get_bounding_box(self, face_sim_rank=0):
        """Get bounding_box
        :rtype: dict
        """
        return self.content_eval.get("faces")[face_sim_rank].get("bounding_box")

    def get_face_id(self, face_sim_rank=0):
        """Get face_id
        :rtype: str
        """
        return self.content_eval.get("faces")[face_sim_rank].get("face_id")

    def get_similarity(self, face_sim_rank=0):
        """Get similarity
        :rtype: float
        """
        return self.content_eval.get("faces")[face_sim_rank].get("similarity")