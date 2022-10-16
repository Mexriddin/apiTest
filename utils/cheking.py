"""Methods for checked response"""
from requests import Response


class Cheking():

    """Method for checked status code"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Successfully!!! Status code = " + str(response.status_code))
        else:
            print("Failed!!! Status code = " + str(response.status_code))
