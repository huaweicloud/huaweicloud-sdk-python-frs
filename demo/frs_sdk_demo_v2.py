# -*- coding: utf-8 -*-

from frsclient import AuthInfo
from frsclient import FrsClient

ak = "Your access key"
sk = "Your secret key"
project_id = "Your project id"

image1_path = "Local image path"
image2_path = "Local image path"

region = "Region"
endpoint = "End point corresponding to region"

if __name__ == '__main__':
    auth_info = AuthInfo(ak=ak, sk=sk, end_point="https://face.apxxx.myhuaweicloud.com")
    frs_client = FrsClient(auth_info=auth_info, project_id=project_id)
    # Compare face
    result = frs_client.get_v2().get_compare_service().compare_face_by_file(image1_path, image2_path)
    print(result.get_eval_result())
    # Detect face
    result = frs_client.get_v2().get_detect_service().detect_face_by_file(image1_path)
    print(result.get_eval_result())
    # Create face set
    result = frs_client.get_v2().get_face_set_service().create_face_set("face_set_name")
    print(result.get_eval_result())
    # Add face
    result = frs_client.get_v2().get_face_service().add_face_by_file("face_set_name", image1_path)
    print(result.get_eval_result())
    # Search face
    result = frs_client.get_v2().get_search_service().search_face_by_file("face_set_name", image2_path)
    print(result.get_eval_result())
