import connexion
import six

from swagger_server.models.latlong import Latlong  # noqa: E501
from swagger_server import util

import geocoder

def get_latitude(address=None):  # noqa: E501
    """Get the latitude and longitude of an address

    Gets an object containing the lattitude and longitude of a street address # noqa: E501

    :param address: The address to look up
    :type address: str

    :rtype: Latlong
    """
    g = geocoder.google(address)
    return Latlong(g.lat, g.lng)
