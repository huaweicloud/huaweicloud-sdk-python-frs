# _*_ coding: utf-8 _*_

class CreateFaceSetResult(object):
    """Result of create face set."""
    
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

    def getFaceSetInfo(self):
        """Get Face set info
        :rtype: dict
        """
        return self.contentEval.get("face_set_info")

    def getCreateDate(self):
        """Get create_date
        :rtype: str 
        """
        return self.contentEval.get("face_set_info").get("create_date")

    def getFaceSetCapacity(self):
        """Get face_set_capacity
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
        """Get external_fields
        :rtype: str
        """
        return self.contentEval.get("face_set_info").get("external_fields")

    def getFaceSetName(self):
        """Get face_set_name
        :rtype: str
        """
        return self.contentEval.get("face_set_info").get("face_set_name")