# _*_ coding: utf-8 _*_

class GetAllFaceSetsResult(object):
    """Result of get all face sets."""
    
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

    def getFaceSetsInfo(self):
        """Get face_sets_info
        :rtype: dict
        """
        return self.contentEval.get("face_sets_info")

    def getCreateDate(self, faceSetIndex=0):
        """Get create_date
        :rtype: str
        """
        return self.contentEval.get("face_sets_info")[faceSetIndex].get("create_date")

    def getFaceSetCapacity(self, faceSetIndex=0):
        """Get capacity
        :rtype: int
        """
        return self.contentEval.get("face_sets_info")[faceSetIndex].get("face_set_capacity")

    def getFaceSetId(self, faceSetIndex=0):
        """Get face_set_id
        :rtype: str
        """
        return self.contentEval.get("face_sets_info")[faceSetIndex].get("face_set_id")

    def getFaceNumber(self, faceSetIndex=0):
        """Get face_number
        :rtype: int
        """
        return self.contentEval.get("face_sets_info")[faceSetIndex].get("face_number")

    def getExternalFields(self, faceSetIndex=0):
        """Get face_number
        :rtype: str
        """
        return self.contentEval.get("face_sets_info")[faceSetIndex].get("external_fields")

    def getFaceSetName(self, faceSetIndex=0):
        """Get face_set_name
        :rtype: str
        """
        return self.contentEval.get("face_sets_info")[faceSetIndex].get("face_set_name")

    def getFaceSetsNumber(self):
        """Get face sets number
        :rtype: int
        """
        return len(self.contentEval.get("face_sets_info"))