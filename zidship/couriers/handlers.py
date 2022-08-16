import requests
from . import constants
class CourierHandler:
    """
        This class handler responsible for handling call couriers APIs
    """

    def call_courier_api(self, url, method, headers={}, data={}, params={}):
        """
            this method responsible for making request to the Courier API
        """
        try:
            response = requests.request(
                method=method, 
                url=url,
                headers=headers, 
                data=data, 
                params=params)

            # Reponse status code in not [200, 201]
            if response.status_code not in constants.ACCEPTED_STATUS_CODE:
                return False, None 

            response_data = response.json()
        except Exception as e:
            return False, str(e)
        return True, response_data
