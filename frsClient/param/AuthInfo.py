# _*_ coding: utf-8 _*_

from common import FrsConstant

class AuthInfo(object):
    """AuthInfo is the class with contains the account information.

    Basic usage::
        >>> authInfo = AuthInfo(ak="your ak", sk="your sk")

    """
    def __init__(self, ak, sk, endPoint=FrsConstant.endPoint, region=FrsConstant.region):
        """ Set AuthInfo

        :param ak: Access Key Id.
        :param sk: Secret Access Key.
        :parm endPoint[Optional]: FRS address
        :param region[optional]: Service area
        """
        self.endPoint = endPoint
        self.region = region
        self.ak = ak
        self.sk = sk