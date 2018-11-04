from swagger_server.custom import CustomGoogleQuery, CustomGoogleReverseQuery
from swagger_server import util
from swagger_server.models.error import Error
from flask import abort
import json

import geocoder 

def interpretResponse(geocoderResult):
    if geocoderResult.status == "OVER_QUERY_LIMIT":
        return Error("Exceeded query limit - OVER_QUERY_LIMIT", 420, "Rate limited"), 420
    if geocoderResult.status == "OVER_DAILY_LIMIT":
        return Error("Exceeded daily limit - OVER_DAILY_LIMIT", 420, "Rate limited"), 420
    if geocoderResult.status == "ZERO_RESULTS":
        return Error("No locations found matching query - ZERO_RESULTS", 404, "Not found"), 404
    if geocoderResult.status == "INVALID_REQUEST" or geocoderResult.status.startswith("ERROR - 400"):
        return Error("Request to maps API was invalid - INVALID_REQUEST", 400, "Bad request"), 400
    if geocoderResult.status != "OK":
        return Error(f"Unkown error with status={geocoderResult.status}", 500, "Internal server error"), 500

    del geocoderResult.json['raw']
    return geocoderResult.json, 200

def interpretError(error):
    return Error(str(error), 400, "Bad request"), 400

def execute(closure):
    try:
        return interpretResponse(closure())
    except Exception as e:
        return interpretError(e)

class GeocoderApi(object):
    def get_locate(self, location, region=None, bounds=None, components=None):
        def closure():
            customArgs = {
                "bounds": (bounds or None) and "|".join(map(str, bounds)),
                "region": (region or None) and region.lower(),
                "components": (components or None) and "|".join(map(str, components))
            }

            return CustomGoogleQuery(location, **customArgs)
            
        return execute(closure)

    def get_reverse_locate(self, latlong, result_type=None):
        def closure():
            customArgs = {
                "result_type": (result_type or None) and "|".join(map(str, result_type))
            }

            return CustomGoogleReverseQuery(latlong.split(','), **customArgs)
            
        return execute(closure)
