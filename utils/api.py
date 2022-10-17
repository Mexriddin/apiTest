from utils.http_methods import Http_methods

base_url = "https://rahulshettyacademy.com"  # base_url
key = "?key=qaclick123"  # params for request

"""Methods for testing GoogleMaps API"""


class Google_maps_api():

    """Method for create new location"""
    @staticmethod
    def create_new_place():
        json_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        path = "/maps/api/place/add/json"
        url = base_url + path + key
        print(url)
        result = Http_methods.post(url=url, body=json_create_new_place)
        print(result.text)
        return result

    """Method for check new location"""
    @staticmethod
    def get_new_place(place_id):
        path = "/maps/api/place/get/json"
        url = base_url + path + key + "&place_id=" + place_id
        print(url)
        result = Http_methods.get(url)
        print(result.text)
        return result

    """Method for change new location"""
    @staticmethod
    def put_new_place(place_id):
        path = "/maps/api/place/update/json"
        url = base_url + path + key
        print(url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result = Http_methods.put(url, json_for_update_new_location)
        print(result.text)
        return result

    """Method for delete new location"""
    @staticmethod
    def delete_new_place(place_id):
        path = "/maps/api/place/delete/json"
        url = base_url + path + key
        print(url)
        json_for_delete_new_location = {
            "place_id": place_id
        }
        result = Http_methods.delete(url, json_for_delete_new_location)
        print(result.text)
        return result