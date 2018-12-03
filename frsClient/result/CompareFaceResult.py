# _*_ coding: utf-8 _*_

class CompareFaceResult(object):
    """Result of compare face."""
    
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

    def getSimilarity(self):
        """Get similarity
        :rtype: float
        """
        return self.contentEval.get("similarity")

    def getImage1Face(self):
        """Get detected face1.
        :rtype: dict
        """
        return self.contentEval.get("image1_face")

    def getImage2Face(self):
        """Get detected face2.
        :rtype: dict
        """
        return self.contentEval.get("image2_face")

    def getImage1BoundingBox(self):
        """Get bounding_box of image1.
        :rtype: dict
        """
        return self.contentEval.get("image1_face").get("bounding_box")

    def getImage2BoundingBox(self):
        """Get bounding_box of image2.
        :rtype: dict
        """
        return self.contentEval.get("image2_face").get("bounding_box")