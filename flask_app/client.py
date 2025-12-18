import requests


class ClasherClient(object):
    def __init__(self):
        self.sess = requests.Session()
        self.base_url = f"http://35.237.27.6:8080/"

    # *********NEED TO FIX********************
    def search_by_player_id(self, id):
        """
        Docstring for search_by_player_id

        Searches the API for the player associated with id.
        
        :param self: Description
        :param id: Description
        """
        endpoint = f'player/{id}'

        # print(self.base_url + endpoint)
        # response = self.sess.get(self.base_url + endpoint)
        
        # if response.status_code == 200:
        #     data = response.json()

            return data
        
        # elif response.status_code == 403:
        # # 403 Forbidden is often a sign of an incorrect IP address or token
        #     raise ValueError(
        #         "Error 403: Forbidden. Check your whitelisted IP address or your API key."
        #     )

        # else:
        #     print(f"Request failed with status code: {response.status_code}")
        #     print("Error Message:", response.text)
        #     raise ValueError(
        #         f"Request failed with status code: {response.status_code}. \n Error Message: {response.text}"
        #     )

        try:
            resp = self.sess.get(self.base_url + endpoint)

            # If status is 200, return the JSON data.
            # *********NEED TO FIX********************
            # FOR NOW, if status is 404 (Not Found), return None so the app doesn't crash, idk why it's not fetching
            if resp.status_code == 200:
                return resp.json()
            else:
                return None
        except:
            return None
        
    # *********NEEDS TWEAKING************
    def get_all_cards(self):
        endpoint = "cards"
        # resp = self.sess.get(self.base_url + endpoint)
        
        # if resp.status_code == 200:
        #     return resp.json() 
        # else:
        #     return []
        
        try:
            resp = self.sess.get(self.base_url + endpoint)
            
            if resp.status_code == 200:
                data = resp.json()

                if isinstance(data, dict) and "items" in data:
                    return data["items"]
                elif isinstance(data, list):
                    return data
                else:
                    return []
            else:
                return []
        except:
            return []
        
        
if __name__ == "__main__":
    import os

    client = ClasherClient()

    player = client.search_by_player_id("YP9JJPJLY")
    cards = client.get_cards()

    print(player["name"])
    print(cards[1])