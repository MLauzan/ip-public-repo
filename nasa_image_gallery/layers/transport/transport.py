# capa de transporte/comunicación con otras interfaces o sistemas externos.

import requests
from ...config import config
from ..generic.utils import pagesQuantity

# comunicación con la REST API de la NASA.
def getAllImages(input=None, page='1'):
    if input is None:
        json_response = requests.get(config.NASA_REST_API_DEFAULT_SEARCH + '&page=' + page +'&page_size=5').json()
    else:
        json_response = requests.get(config.NASA_REST_API + input + '&page=' + page +'&page_size=5').json()

    json_collection = []
    
    pages = pagesQuantity(json_response['collection']['metadata']['total_hits'])
            
    for object in json_response['collection']['items']:
        try:
            if 'links' not in object:
                object['links'] = [{'href': 'https://w7.pngwing.com/pngs/707/497/png-transparent-globe-world-map-earth-globe-miscellaneous-globe-grey.png'}]
  
            json_collection.append(object)

        except KeyError:
            pass

    return json_collection, pages