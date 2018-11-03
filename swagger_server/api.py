from swagger_server.custom import CustomGoogleQuery
from swagger_server.models.latlong import Latlong  # noqa: E501
from swagger_server import util

class GeocoderApi(object):
    def get_locate(self, address=None, northeast=None, southwest=None):
        g = CustomGoogleQuery(address, northeast=northeast, southwest=southwest)
        return Latlong(g.lat, g.lng)
