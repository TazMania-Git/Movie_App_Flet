import requests
import json
import sys

### FUNCIONA #####
sys.path.append(r'F:\Flet Flutter Apps\App\Movie_App_Flet\models') ###cambiar el directorio es alta paja
import now_playing_response as np
##################r

response_API = requests.get(url='https://api.themoviedb.org/3/movie/now_playing?api_key=19c0cd86b94cabbe32dfa1440e41e8f9&language=es-ES&page=1')
data = response_API.text
result = np.Moviesfromdict(json.loads(data))
result.results[0].title
# models.now_playing_response