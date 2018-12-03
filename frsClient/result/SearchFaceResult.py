# _*_ coding: utf-8 _*_

class SearchFaceResult(object):
    """Result of search face."""
    
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

    def getFaces(self):
        """Get faces
        :rtype: list
        """
        return self.contentEval.get("faces")

    def getExternalImageId(self, faceSimRank=0):
        """Get external_image_id
        :rtype: str
        """
        return self.contentEval.get("faces")[faceSimRank].get("external_image_id")

    def getBoundingBox(self, faceSimRank=0):
        """Get bounding box
        :rtype: dict
        """
        return self.contentEval.get("faces")[faceSimRank].get("bounding_box")

    def getFaceId(self, faceSimRank=0):
        """Get face_id
        :rtype: str
        """
        return self.contentEval.get("faces")[faceSimRank].get("face_id")

    def getSimilarity(self, faceSimRank=0):
        """Get similarity
        :rtype: float
        """
        return self.contentEval.get("faces")[faceSimRank].get("similarity")