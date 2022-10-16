from requests import Response
from utils.cheking import Cheking

from utils.api import Google_maps_api

"""Create, Update and Delete new location"""


class Test_create_place():

    def test_create_new_place(self):
        print("\nMethod POST")
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post["place_id"]
        Cheking.check_status_code(result_post, 200)

        print("\nMethod GET->POST")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)

        print("\nMethod PUT")
        result_put: Response = Google_maps_api.put_new_place(place_id)
        Cheking.check_status_code(result_put, 200)

        print("\nMethod GET->PUT")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)

        print("\nMethod DELETE")
        result_delete: Response = Google_maps_api.delete_new_place(place_id)
        Cheking.check_status_code(result_delete, 200)

        print("\nMethod GET->DELETE")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 404)
