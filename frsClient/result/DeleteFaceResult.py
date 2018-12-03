# _*_ coding: utf-8 _*_

class DeleteFaceResult(object):
    """Result of delete face."""
    
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
    
    def getFaceNumber(self):
        """Get number deleted
        :rtype: int
        """
        return self.contentEval.get("face_number")

    def getFaceSetId(self):
        """Get face_set_id 
        :rtype: str
        """
        return self.contentEval.get("face_set_id")

    def getFaceSetName(self):
        """Get face set name
        :rtype: str
        """
        return self.contentEval.get("face_set_name")