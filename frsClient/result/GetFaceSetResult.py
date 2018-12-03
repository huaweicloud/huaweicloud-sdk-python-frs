# _*_ coding: utf-8 _*_

class GetFaceSetResult(object):
    """Result of get face set."""
    
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

    def getCreateDate(self):
        """Get create data
        :rtype: str
        """
        return self.contentEval.get("face_set_info").get("create_date")

    def getFaceSetInfo(self):
        """Get face_set_info
        :rtype: dict
        """
        return self.contentEval.get("face_set_info")

    def getFaceSetCapacity(self):
        """Get capacity
        :rtype: int
        """
        return self.contentEval.get("face_set_info").get("face_set_capacity")

    def getFaceSetId(self):
        """Get face_set_id
        :rtype: str
        """
        return self.contentEval.get("face_set_info").get("face_set_id")

    def getFaceNumber(self):
        """Get face_number
        :rtype: int
        """
        return self.contentEval.get("face_set_info").get("face_number")

    def getExternalFields(self):
        """Get external fields
        :rtype: str
        """
        return self.contentEval.get("face_set_info").get("external_fields")

    def getFaceSetName(self):
        """Get face_set_name
        :rtype: str
        """
        return self.contentEval.get("face_set_info").get("face_set_name")