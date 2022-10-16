from utils.http_methods import Http_methods

base_url = "https://rahulshettyacademy.com"  # base_url
key = "?key=qaclick123"                      # params for request

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
        print(base_url)
        result = Http_methods.post(url=url, body=json_create_new_place)
        print(result.text)
        return result

    @staticmethod
    def get_new_place(place_id):
        path = "/maps/api/place/get/json"
        url = base_url + path + "&place_id=" + place_id
        print(url)
        result = Http_methods.get(url)
        print(result.text)
        return result
