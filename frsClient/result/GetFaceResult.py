# _*_ coding: utf-8 _*_

class GetFaceResult(object):
    """Result of get face."""
    
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

    def getFaceSetName(self):
        """Get face set name
        :rtype: str
        """
        return self.contentEval.get("face_set_name")

    def getFaceSetId(self):
        """Get face_set_id
        :rtype: str
        """
        return self.contentEval.get("face_set_id")

    def getFaces(self):
        """Get faces
        :rtype: list
        """
        return self.contentEval.get("faces")

    def getFaceId(self, faceIndex=0):
        """Get face_id
        :rtype: str
        """
        return self.contentEval.get("faces")[faceIndex].get("face_id")

    def getExternalImageId(self, faceIndex=0):
        """Get external image id
        :rtype: str
        """
        return self.contentEval.get("faces")[faceIndex].get("external_image_id")

    def getExternalFields(self, faceIndex=0):
        """Get external_fields
        :rtype: str
        """
        return self.contentEval.get("faces")[faceIndex].get("external_fields")

    def getBoundingBox(self, faceIndex=0):
        """Get bounding_box of nth face
        :rtype: dict
        """
        return self.contentEval.get("faces")[faceIndex].get("bounding_box")