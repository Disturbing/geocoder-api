import connexion
import six

from swagger_server import util
from swagger_server.api import GeocoderApi
api = GeocoderApi()

def get_forward(location, region=None, bounds=None, components=None):  # noqa: E501
    """Forward geocoding

    Does forward geocoding # noqa: E501

    :param location: A string value of the location you are geocoding. See  https://developers.google.com/maps/faq#geocoder_queryformat for reference.
    :type location: str
    :param region: A 2 letter string value of the region you would like to query, see https://developers.google.com/maps/documentation/geocoding/intro#RegionCodes for reference.
    :type region: str
    :param bounds: A string value denoting a bounding box to focus the search within. The bounds parameter defines the latitude/longitude coordinates of the southwest and northeast corners of this bounding box using a pipe (|) character to separate the coordinates. See  https://developers.google.com/maps/documentation/geocoding/intro#Viewports
    :type bounds: List[str]
    :param components: A list of string values specifying component restrictions.  Available filters are postal_code, country, route, locality, administrative_area. See https://developers.google.com/maps/documentation/geocoding/intro#ComponentFiltering for reference.
    :type components: List[str]

    :rtype: None
    """
    return api.get_locate(location, region, bounds, components)


def get_reverse(latlong):  # noqa: E501
    """Reverse geocoding

    Does reverse geocoding # noqa: E501

    :param latlong: The latitude/longitude pair to resolve.
    :type latlong: str

    :rtype: None
    """
    return api.get_reverse_locate(latlong)
