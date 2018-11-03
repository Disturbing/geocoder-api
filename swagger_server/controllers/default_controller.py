import connexion
import six

from swagger_server.models.latlong import Latlong  # noqa: E501
from swagger_server import util
from swagger_server.api import GeocoderApi
api = GeocoderApi()

def get_locate(address=None, northeast=None, southwest=None):  # noqa: E501
    """Get the latitude and longitude of an address

    Gets an object containing the lattitude and longitude of a street address # noqa: E501

    :param address: The address to look up
    :type address: str
    :param northeast: 
    :type northeast: List[]
    :param southwest: 
    :type southwest: List[]

    :rtype: Latlong
    """

    return api.get_locate(address, northeast, southwest)
