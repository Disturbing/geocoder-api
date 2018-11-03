from swagger_server.custom import CustomGoogleQuery
from swagger_server import util

def csv(list):
    if list == None:
        return None
    return ','.join(map(str, list)) 

class GeocoderApi(object):
    def get_locate(self, location=None, region=None, bounds=None, components=None):
        customArgs = {
            "bounds": (bounds or None) and "|".join(map(str, bounds)),
            "region": (region or None) and region.lower(),
            "components": (components or None) and "|".join(map(str, components))
        }

        g = CustomGoogleQuery(location, **customArgs)
        print(g.url)
        return g.json
