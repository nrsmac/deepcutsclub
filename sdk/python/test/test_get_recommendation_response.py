# coding: utf-8

"""
    Deepcuts API

    An API to access music artist metadata and recommendations.

    The version of the OpenAPI document: v0.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from deepcuts_sdk.models.get_recommendation_response import GetRecommendationResponse  # noqa: E501


class TestGetRecommendationResponse(unittest.TestCase):
    """GetRecommendationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetRecommendationResponse:
        """Test GetRecommendationResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetRecommendationResponse`
        """
        model = GetRecommendationResponse()  # noqa: E501
        if include_optional:
            return GetRecommendationResponse(
                albums = [
                    deepcuts_sdk.models.album.Album(
                        title = '',
                        artist_name = '',
                        spotify_id = '',
                        spotify_url = '',
                        discogs_release_id = 56,
                        image_url = '',
                        credit_artist_ids = [
                            56
                            ], )
                    ]
            )
        else:
            return GetRecommendationResponse(
                albums = [
                    deepcuts_sdk.models.album.Album(
                        title = '',
                        artist_name = '',
                        spotify_id = '',
                        spotify_url = '',
                        discogs_release_id = 56,
                        image_url = '',
                        credit_artist_ids = [
                            56
                            ], )
                    ],
        )
        """

    def testGetRecommendationResponse(self):
        """Test GetRecommendationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
