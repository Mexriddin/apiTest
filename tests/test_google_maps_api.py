import allure
from requests import Response
from utils.checking import Checking
from utils.api import Google_maps_api

"""Create, Update and Delete new location"""


@allure.epic("Test create place")
class Test_create_place():

    @allure.description("Test create, update and delete new place")
    def test_create_new_place(self):
        print("\nMethod POST")
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post["place_id"]
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

        print("\nMethod GET->POST")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number',
                                               'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print("\nMethod PUT")
        result_put: Response = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("\nMethod GET->PUT")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number',
                                               'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("\nMethod DELETE")
        result_delete: Response = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print("\nMethod GET->DELETE")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')

        print("Testing create, update and delete new location successfully")
