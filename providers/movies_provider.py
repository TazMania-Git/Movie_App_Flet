import requests
import json
import sys
### FUNCIONA #####
# sys.path.append(r'E:\Mis Documentos\Flet Flutter apps\Movie_App_Flet\models')
# import now_playing_response
##################

import models
# import models.now_playing_response as now
# from models import now_playing_response



response_API = requests.get(url='https://api.themoviedb.org/3/movie/now_playing?api_key=19c0cd86b94cabbe32dfa1440e41e8f9&language=es-ES&page=1')
data = response_API.text
result = now_playing_response .Moviesfromdict(json.loads(data))
result.results[0].title
models.now_playing_response