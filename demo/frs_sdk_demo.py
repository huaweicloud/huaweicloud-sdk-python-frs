# -*- coding: utf-8 -*-

from frsclient import FrsClient
from frsclient import AuthInfo


## Set initial Auth Information
ak = "*** Your AK ***"
sk = "*** Your SK ***"
project_id = "*** Your project ID ***"

## Set initial vars.
picture1_file = "*** File path ***"
picture2_file = "*** File path ***"
video_file = "*** File path ***"
import base64
with open(video_file, 'rb') as f:
    video_base64 = base64.b64encode(f.read())
live_actions = "*** Actions ***"
face_set_name = "*** Your face set name ***"
create_face_set_external_fields = {"number":{"type":"integer"}, "id":{"type":"string"}, "timestamp":{"type":"long"}}
add_face_external_fields = {"timestamp":12, "id": "home"}

## Initializes the FRS frsclient. 2 ways, choose 1.
## (1)
frs_client = FrsClient(ak=ak, sk=sk, project_id=project_id)
## (2)
auth_info = AuthInfo(ak=ak, sk=sk, end_point="https://face.cn-north-1.myhuaweicloud.com")
frs_client = FrsClient(auth_info=auth_info, project_id=project_id)

# def service_query_example(frs_client):
result_service_query = frs_client.get_service_query().service_query()
print(result_service_query.get_eval_result())
print(result_service_query.get_max_face_set_number())

# def face_detect_example(frs_client):
result_detect = frs_client.get_detect_service().detect_face_by_file(picture1_file)
print(result_detect.get_eval_result())
print(result_detect.get_faces())
print(result_detect.get_bounding_box(0))

# def face_compare_example(frs_client):
result_compare = frs_client.get_compare_service().compare_face_by_file(picture1_file, picture2_file)
print(result_compare.get_eval_result())
print(result_compare.get_similarity())
print(result_compare.get_image1_face())
print(result_compare.get_image2_face())

# def live_detect_by_file_example(frs_client, video_file, live_actions):
result_live = frs_client.get_live_detect_service().live_detect_by_file(video_file, live_actions)
print(result_live.get_eval_result())
print(result_live.get_alive())
print(result_live.get_actions())
print(result_live.get_warning_list())

# def live_detect_by_base64_example(frs_client, video_base64, live_actions):
result_live2 = frs_client.get_live_detect_service().live_detect_by_base64(video_base64, live_actions)
print(result_live2.get_eval_result())
print(result_live2.get_alive())
print(result_live2.get_actions())
print(result_live2.get_warning_list())

# def create_face_set_example(frs_client, face_set_name, create_face_set_external_fields):
result_create_face_set = frs_client.get_face_set_service().create_face_set(face_set_name, external_fields=create_face_set_external_fields)
print(result_create_face_set.get_eval_result())
print(result_create_face_set.get_face_set_info())
print(result_create_face_set.get_create_date())
print(result_create_face_set.get_face_set_capacity())
print(result_create_face_set.get_face_number())

# def get_face_set_example(frs_client, face_set_name):
result_get_face_set = frs_client.get_face_set_service().get_face_set(face_set_name)
print(result_get_face_set.get_eval_result())
print(result_get_face_set.get_face_set_info())
print(result_get_face_set.get_external_fields())
print(result_get_face_set.get_face_set_capacity())
print(result_get_face_set.get_create_date())

# def get_all_face_sets_example(frs_client):
result_get_all_face_sets = frs_client.get_face_set_service().get_all_face_sets()
print(result_get_all_face_sets.get_eval_result())
print(result_get_all_face_sets.get_face_sets_number())
print(result_get_all_face_sets.get_face_set_id(0))
print(result_get_all_face_sets.get_face_set_capacity(0))
print(result_get_all_face_sets.get_create_date(0))

# def delete_face_set_example(frs_client, face_set_name):
result_delete_face_set = frs_client.get_face_set_service().delete_face_set(face_set_name)
print(result_delete_face_set.get_eval_result())
print(result_delete_face_set.get_face_set_name())

# def add_face_example(frs_client, face_set_name, picture1_file, external_fields=None):
result_add_face = frs_client.get_face_service().add_face_by_file(face_set_name, picture1_file, external_fields=add_face_external_fields)
print(result_add_face.get_eval_result())
print(result_add_face.get_faces())
face_id = result_add_face.get_face_id()
print(result_add_face.get_face_id())
print(result_add_face.get_bounding_box())

# def get_face_example(frs_client, face_set_name, face_id):
result_get_face = frs_client.get_face_service().get_face(face_set_name, face_id)
print(result_get_face.get_eval_result())
print(result_get_face.get_faces())

# def get_faces_example(frs_client, face_set_name):
result_get_faces = frs_client.get_face_service().get_faces(face_set_name, offset=0, limit=5)
print(result_get_faces.get_eval_result())
print(result_get_faces.get_faces())
print(result_get_faces.get_face_id(0))
print(result_get_faces.get_external_image_id(0))
print(result_get_faces.get_bounding_box(0))
print(result_get_faces.get_external_fields(0))

# def delete_face_example(frs_client, face_set_name, face_id):
result_delete_face = frs_client.get_face_service().delete_face_by_face_id(face_set_name, face_id)
print(result_delete_face.get_eval_result())
print(result_delete_face.get_face_set_name())
print(result_delete_face.get_face_number())

# def search_face_example(frs_client, face_set_name, picture2_file):
result_search = frs_client.get_search_service().search_face_by_file(face_set_name, picture2_file)
print(result_search.get_eval_result())
print(result_search.get_bounding_box())
print(result_search.get_faces())
print(result_search.get_face_id())
print(result_search.get_similarity())
