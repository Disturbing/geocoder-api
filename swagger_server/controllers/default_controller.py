import connexion
import six

from swagger_server import util
from swagger_server.api import GeocoderApi
server = GeocoderApi()

def get_forward(location=None, region=None, bounds=None, components=None):  # noqa: E501
    """Forward geocoding

    Does forward geocoding # noqa: E501

    :param location: A string value of the location you are geocoding. See  https://developers.google.com/maps/faq#geocoder_queryformat for reference.
    :type location: str
    :param region: A 2 letter string value of the region you would like to query, see https://developers.google.com/maps/documentation/geocoding/intro#RegionCodes for reference.
    :type region: str
    :param bounds: A string value denoting a bounding box to focus the search within. The bounds parameter defines the latitude/longitude coordinates of the southwest and northeast corners of this bounding box using a pipe (|) character to separate the coordinates. See  https://developers.google.com/maps/documentation/geocoding/intro#Viewports for reference.
    :type bounds: str
    :param components: A string value restricting the search to a specified area. A filter consists of a list of component:value pairs separated by a pipe (|). Available filters are postal_code, country, route, locality, administrative_area. See https://developers.google.com/maps/documentation/geocoding/intro#ComponentFiltering for reference.
    :type components: str

    :rtype: None
    """
    return server.get_locate(location, region, bounds, components)
