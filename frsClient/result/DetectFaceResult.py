# _*_ coding: utf-8 _*_

class DetectFaceResult(object):
    """Result of detect face."""
    
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

    def getBoundingBox(self, faceIndex=0):
        """Get bounding box
        :rtype: dict
        """
        return self.contentEval.get("faces")[faceIndex].get("bounding_box")