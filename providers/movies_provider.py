import requests
import json
import models.now_playing_response as now_playing_response

response_API = requests.get(url='https://api.themoviedb.org/3/movie/now_playing?api_key=19c0cd86b94cabbe32dfa1440e41e8f9&language=es-ES&page=1')
#print(response_API.status_code)
data = response_API.text
# parse_json = json.loads(data)
result = now_playing_response.Welcomefromdict(json.loads(data))
result.results[0].title