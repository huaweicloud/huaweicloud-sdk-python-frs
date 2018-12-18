# -*- coding: utf-8 -*-

class CompareFaceResult(object):
    """Result of compare face."""
    
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

    def get_similarity(self):
        """Get similarity
        :rtype: float
        """
        return self.content_eval.get("similarity")

    def get_image1_face(self):
        """Get detected face1.
        :rtype: dict
        """
        return self.content_eval.get("image1_face")

    def get_image2_face(self):
        """Get detected face2.
        :rtype: dict
        """
        return self.content_eval.get("image2_face")

    def get_image1_bounding_box(self):
        """Get bounding_box of image1.
        :rtype: dict
        """
        return self.content_eval.get("image1_face").get("bounding_box")

    def get_image2_bounding_box(self):
        """Get bounding_box of image2.
        :rtype: dict
        """
        return self.content_eval.get("image2_face").get("bounding_box")