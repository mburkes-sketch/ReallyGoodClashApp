import requests

API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjRiMjE3YTZlLTZlYjQtNDk1NC1iNTdmLTBjNTRmODhiMWVmMSIsImlhdCI6MTc2NTAzNzY2MCwic3ViIjoiZGV2ZWxvcGVyL2EyYzJjOTVhLWE2MzAtYTEyZC1hZmY4LTBlNjJjZThhODM2NCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1MC4xNDQuMjEzLjIyNiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.LcgiQGWGQa72eGuSX1ATkUxsL1xewxqcZzwTpv3hGyQ1T6usn4UPU0gSKXPWEVus0lBHrrpEhFcwjT3-mptc-w"

import requests


# 2. Define the Base URL and the specific endpoint
BASE_URL = 'https://api.clashroyale.com/v1'
PLAYER_TAG = '#8QJJJ0C'  # Example Player Tag (Must start with #)
ENDPOINT = '/cards' 


class ClasherClient(object):
    def __init__(self):
        self.sess = requests.Session()
        self.base_url = f"http://35.237.27.6:8080/"

    def search_by_player_id(self, id):
        """
        Docstring for search_by_player_id

        Searches the API for the player associated with id.
        
        :param self: Description
        :param id: Description
        """
        endpoint = f'player/{id}'

        print(self.base_url + endpoint)
        response = self.sess.get(self.base_url + endpoint)
        
        if response.status_code == 200:
            data = response.json()

            return data["name"]
        
        elif response.status_code == 403:
        # 403 Forbidden is often a sign of an incorrect IP address or token
            raise ValueError(
                "Error 403: Forbidden. Check your whitelisted IP address or your API key."
            )

        else:
            print(f"Request failed with status code: {response.status_code}")
            print("Error Message:", response.text)
            raise ValueError(
                f"Request failed with status code: {response.status_code}. \n Error Message: {response.text}"
            )
        
        
if __name__ == "__main__":
    import os

    client = ClasherClient()

    name = client.search_by_player_id("YP9JJPJLY")

    print(name)