from swagger_server.custom import CustomGoogleQuery
from swagger_server import util

def csv(list):
    if list == None:
        return None
    return ','.join(map(str, list)) 

class GeocoderApi(object):
    def get_locate(self, location=None, region=None, bounds=None, components=None):
        customArgs = {
            "bounds": bounds
        }

        g = CustomGoogleQuery(location, **customArgs)
        print(g.url)
        return g.json
