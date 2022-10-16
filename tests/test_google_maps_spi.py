from requests import Response

from utils.api import Google_maps_api

"""Create, Update and Delete new location"""


class Test_create_place():

    def test_create_new_place(self):
        print("\nMethod POST")
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post["place_id"]

        print("\nMethod GET->POST")
        result_get: Response = Google_maps_api.get_new_place(place_id)

        print("\nMethod PUT")
        result_out: Response = Google_maps_api.put_new_place(place_id)

        print("\nMethod GET->PUT")
        result_get: Response = Google_maps_api.get_new_place(place_id)

        print("\nMethod DELETE")
        result_delete: Response = Google_maps_api.delete_new_place(place_id)

        print("\nMethod GET->DELETE")
        result_get: Response = Google_maps_api.get_new_place(place_id)