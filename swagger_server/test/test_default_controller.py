# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.test import BaseTestCase

import json

class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_forward_location(self):
        """Test case for get_forward

        Forward geocoding
        """
        query_string = [('location', 'santa cruz')]
        response = self.client.open(
            '/geocoder/forward',
            method='GET',
            query_string=query_string)
        assert json.loads(response.data.decode('utf-8'))["city"] == "Santa Cruz"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_forward_no_location(self):
        """Test case for get_forward with no location (error)

        Forward geocoding
        """
        query_string = [('region', 'region_example'),
                        ('bounds', 'bounds_example'),
                        ('components', 'components_example')]
        response = self.client.open(
            '/geocoder/forward',
            method='GET',
            query_string=query_string)
        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_forward_region(self):
        """Test case for get_forward with region

        Forward geocoding
        """
        # no region
        query_string = [('location', 'santa cruz')]
        response = self.client.open(
            '/geocoder/forward',
            method='GET',
            query_string=query_string)
        assert json.loads(response.data.decode('utf-8'))["city"] == "Santa Cruz"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # region
        query_string = [('location', 'santa cruz'),
                        ('region', 'es')]
        response = self.client.open(
            '/geocoder/forward',
            method='GET',
            query_string=query_string)
        assert json.loads(response.data.decode('utf-8'))["city"] == "Madrid"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_forward_bounds(self):
        """Test case for get_forward with bounds

        Forward geocoding
        """
        # no bounds
        query_string = [('location', 'Winnetka')]
        response = self.client.open(
            '/geocoder/forward',
            method='GET',
            query_string=query_string)
        assert json.loads(response.data.decode('utf-8'))["county"] == "Cook County"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        # bounds
        query_string = [('location', 'Toledo'), ('bounds', '34.172684,-118.604794|34.236144,-118.500938')]
        response = self.client.open(
            '/geocoder/forward',
            method='GET',
            query_string=query_string)
        assert json.loads(response.data.decode('utf-8'))["county"] == "Lucas County"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))



    # def test_get_forward_components(self):
    #     """Test case for get_forward with components

    #     Forward geocoding
    #     """
    #     query_string = [('location', 'location_example'),
    #                     ('components', 'components_example')]
    #     response = self.client.open(
    #         '/geocoder/forward',
    #         method='GET',
    #         query_string=query_string)
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))

    # def test_get_reverse(self):
    #     """Test case for get_reverse

    #     Reverse geocoding
    #     """
    #     query_string = [('latlong', 'latlong_example')]
    #     response = self.client.open(
    #         '/geocoder/reverse',
    #         method='GET',
    #         query_string=query_string)
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))
    def test_get_reverse_with_valid_input_returns_200_with_location(self):
        query_string = [('latlong', '38.438102,-94.226957')]
        response = self.client.open(
            '/geocoder/reverse',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        assert json.loads(response.data.decode('utf-8'))["address"] == "NE County Rd 15004, Garden City, MO 64747, USA"

    def test_get_reverse_returns_404_with_nowhere_location(self):
        query_string = [('latlong', '1,1')]
        response = self.client.open(
            '/geocoder/reverse',
            method='GET',
            query_string=query_string)
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_reverse_returns_400_with_nonsense_location(self):
        query_string = [('latlong', '10000,1')]
        response = self.client.open(
            '/geocoder/reverse',
            method='GET',
            query_string=query_string)
        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_reverse_respects_type(self):
        query_string = [('latlong', '38.438102,-94.226957'), ('result_type', 'political')]
        response = self.client.open(
            '/geocoder/reverse',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        assert json.loads(response.data.decode('utf-8'))["address"] == "Grand River Township, MO, USA"

    def test_get_reverse_reports_upstream_400(self):
        query_string = [('latlong', '38.438102,-94.226957'), ('result_type', 'somecompletelyinvalidvalue')]
        response = self.client.open(
            '/geocoder/reverse',
            method='GET',
            query_string=query_string)
        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))

if __name__ == '__main__':
    import unittest
    unittest.main()
