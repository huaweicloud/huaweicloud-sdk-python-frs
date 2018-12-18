# -*- coding: utf-8 -*-

from frscommon import FrsConstant

class AuthInfo(object):
    """AuthInfo is the class with contains the account information.

    Basic usage::
        >>> auth_info = AuthInfo(ak="your ak", sk="your sk")

    """
    def __init__(self, ak, sk, end_point=FrsConstant.END_POINT, region=FrsConstant.REGION):
        """

        :param ak: Access Key Id.
        :param sk: Secret Access Key.
        :param end_point: [Optional] FRS address
        :param region:    [Optional] Service area
        """
        self.end_point = end_point
        self.region = region
        self.ak = ak
        self.sk = sk