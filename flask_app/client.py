import requests

API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImJlMGFkODI1LTYzNmYtNDcxMC1hZTRmLTc5M2Q2NDk2MzgzMiIsImlhdCI6MTc2NDk2NzkxMCwic3ViIjoiZGV2ZWxvcGVyL2EyYzJjOTVhLWE2MzAtYTEyZC1hZmY4LTBlNjJjZThhODM2NCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxMjkuMi44OS43NSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.nuu500BNHwrqDejdOcvvTrCmN44iAAhN61JzPjdWlzghVAJcI7QMig3mETaEAzRfaXSreZk1wIRZ6E5tql4Sjw"

import requests


# 2. Define the Base URL and the specific endpoint
BASE_URL = 'https://api.clashroyale.com/v1'
PLAYER_TAG = '#8QJJJ0C'  # Example Player Tag (Must start with #)
ENDPOINT = '/cards' 


class ClasherClient(object):
    def __init__(self, api_key):
        self.sess = requests.Session()
        self.base_url = f"https://api.clashroyale.com/v1"
        self.headers = {
            'Authorization': f'Bearer {api_key}'
        }

    def search_by_player_id(self, id):
        """
        Docstring for search_by_player_id

        Searches the API for the player associated with id.
        
        :param self: Description
        :param id: Description
        """
        endpoint = f'/players/{id}'

        response = self.sess.get(self.base_url + endpoint, headers=self.headers)
        
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

    client = ClasherClient("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjA2NmM2MzAyLWE3NTYtNDI2Ni1hOTMyLTc0ZTc4NWQzNjI1YiIsImlhdCI6MTc2Mzk5ODY5Mywic3ViIjoiZGV2ZWxvcGVyL2EyYzJjOTVhLWE2MzAtYTEyZC1hZmY4LTBlNjJjZThhODM2NCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxMjkuMi44OS40NyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.2QRR4Raq2d3dQME-F1rhogmmxTP4L-dOZubqbvg8hlHIrprgh4cfmhZQhZlTzvmSbVbTjST_7X8DFbB4AzEMoQ")

    name = client.search_by_player_id("YP9JJPJLY")

    print(name)