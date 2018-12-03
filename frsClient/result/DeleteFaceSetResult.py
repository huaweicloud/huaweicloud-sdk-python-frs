# _*_ coding: utf-8 _*_

class DeleteFaceSetResult(object):
    """Result of delete face set."""
    
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
        """Get face_set_name.
        :rtype: str
        """
        return self.contentEval.get("face_set_name")