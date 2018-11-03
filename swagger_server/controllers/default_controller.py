import connexion
import six

from swagger_server import util
from swagger_server.api import GeocoderApi
api = GeocoderApi()

def get_forward(location=None, region=None, bounds=None, components=None):  # noqa: E501
    """Forward geocoding

    Does forward geocoding # noqa: E501

    :param location: A string value of the location you are geocoding. See  https://developers.google.com/maps/faq#geocoder_queryformat for reference.
    :type location: str
    :param region: A 2 letter string value of the region you would like to query, see https://developers.google.com/maps/documentation/geocoding/intro#RegionCodes for reference.
    :type region: str
    :param bounds: The south-west and north-east lat/long points defining a box to search within See https://developers.google.com/maps/documentation/geocoding/intro#Viewports  for reference.
    :type bounds: List[str]
    :param components: A list of string values specifying component restrictions.  Available filters are postal_code, country, route, locality, administrative_area. See https://developers.google.com/maps/documentation/geocoding/intro#ComponentFiltering for reference.
    :type components: List[str]

    :rtype: None
    """
    return api.get_locate(location, region, bounds, components)
