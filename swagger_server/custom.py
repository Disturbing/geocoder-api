from geocoder.google import GoogleQuery
from geocoder.google_reverse import GoogleReverse

class CustomGoogleQuery(GoogleQuery):
    def _location_init(self, location, **kwargs):
        defaultArgs = super(CustomGoogleQuery, self)._location_init(location, **kwargs)
        for key, value in kwargs.items():
            if not key in defaultArgs:
                defaultArgs[key] = value

        return defaultArgs

class CustomGoogleReverseQuery(GoogleReverse):
    def _location_init(self, location, **kwargs):
        defaultArgs = super(CustomGoogleReverseQuery, self)._location_init(location, **kwargs)
        for key, value in kwargs.items():
            if not key in defaultArgs:
                defaultArgs[key] = value

        return defaultArgs
