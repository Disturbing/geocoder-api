from swagger_server.custom import CustomGoogleQuery
from swagger_server import util

import geocoder 

class GeocoderApi(object):
    def get_locate(self, location, region=None, bounds=None, components=None):
        customArgs = {
            "bounds": (bounds or None) and "|".join(map(str, bounds)),
            "region": (region or None) and region.lower(),
            "components": (components or None) and "|".join(map(str, components))
        }

        g = CustomGoogleQuery(location, **customArgs)
        print(g.url)
        return g.json

    def get_reverse_locate(self, latitude, longitude):
        g = geocoder.google([latitude, longitude], method='reverse')
        print(g.url)
        return g.json