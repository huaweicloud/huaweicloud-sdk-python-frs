# _*_ coding: utf-8 _*_

from frsClient import FrsClient
from frsClient import AuthInfo

ak = "ak"
sk = "sk"
projectId = "project id"
endPoint = "https://face.cn-north-1.myhuaweicloud.com"
proxyHostInfo = {
    "http": "http://yourDomainName:yourDomainPassword@domain:port",
    "https": "http://yourDomainName:yourDomainPassword@domain:port"
}

# init client
authInfo = AuthInfo(ak, sk, endpoint)
frsClient = FrsClient(authInfo=authInfo, projectId=projectId, proxyHostInfo=proxyHostInfo)

# Use service
detect_result = frsClient.getDetectService().detectFaceByFile("imageFile", "0,1,2,3")
print detect_result.getOriginalResult()

compare_result = frsClient.getCompareService().compareFaceByFile("image1File", "image2File")
print compare_result.getOrginalResult()"
