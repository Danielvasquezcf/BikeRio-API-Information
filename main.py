import requests 
from pprint import pprint 

def get_api_info():
    if __name__ == '__main__':
        url = 'https://api.citybik.es/v2/networks/bikerio'
        response = requests.get(url)
    
        if response.status_code == 200:
            response_json = response.json()
            pprint(response_json)
            
get_api_info()