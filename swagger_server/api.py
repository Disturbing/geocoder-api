from swagger_server.custom import CustomGoogleQuery, CustomGoogleReverseQuery
from swagger_server import util
import json

import geocoder 

def interpretResponse(geocoderResult):
    if geocoderResult.json == None:
        return "Make this into a 404 somehow"
    geocoderResult.json["raw"] = None
    return geocoderResult.json

class GeocoderApi(object):
    def get_locate(self, location, region=None, bounds=None, components=None):
        customArgs = {
            "bounds": (bounds or None) and "|".join(map(str, bounds)),
            "region": (region or None) and region.lower(),
            "components": (components or None) and "|".join(map(str, components))
        }

        g = CustomGoogleQuery(location, **customArgs)
        print(g.url)
        return interpretResponse(g)

    def get_reverse_locate(self, latlong, result_type=None):
        customArgs = {
            "result_type": (result_type or None) and "|".join(map(str, result_type))
        }

        g = CustomGoogleReverseQuery(latlong.split(','), **customArgs)
        print(g.url)
        return interpretResponse(g)
