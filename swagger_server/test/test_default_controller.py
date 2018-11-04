# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501

class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_forward(self):
        """Test case for get_forward

        Forward geocoding
        """
        query_string = [('location', 'location_example'),
                        ('region', 'region_example'),
                        ('bounds', 'bounds_example'),
                        ('components', 'components_example')]
        response = self.client.open(
            '/geocoder/forward',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_reverse(self):
        """Test case for get_reverse

        Reverse geocoding
        """
        query_string = [('latlong', 'latlong_example')]
        response = self.client.open(
            '/geocoder/reverse',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
