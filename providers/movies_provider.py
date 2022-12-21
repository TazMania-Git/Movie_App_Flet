import requests
import json
import sys
sys.path.insert(0,r'models')
import now_playing_response as np

class Movie_provider:
    def __init__(self) -> None:
        self.apiurl = 'https://api.themoviedb.org/3/movie'
    
    def get_all_now_playing(self):
        response_API = requests.get(url=f'{self.apiurl}/now_playing?api_key=19c0cd86b94cabbe32dfa1440e41e8f9&language=es-ES&page=1')
        data = response_API.text
        result = np.Moviesfromdict(json.loads(data))
        return result

''' OLD
### FUNCIONA #####
# sys.path.append(r'F:\Flet Flutter Apps\App\Movie_App_Flet\models') ###cambiar el directorio es alta paja
##################r
# result.results[0].title
# models.now_playing_response
'''