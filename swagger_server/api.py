from swagger_server.custom import CustomGoogleQuery
from swagger_server.models.latlong import Latlong  # noqa: E501
from swagger_server import util

def csv(list):
    if list == None:
        return None
    return ','.join(map(str, list)) 

class GeocoderApi(object):
    def get_locate(self, address=None, northeast=None, southwest=None):
        g = CustomGoogleQuery(address, bounds=f"{csv(southwest)}|{csv(northeast)}")
        return Latlong(g.lat, g.lng)
