# coding: utf-8

"""
    Deepcuts API

    An API to access music artist metadata and recommendations.

    The version of the OpenAPI document: v0.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from deepcuts_sdk.api.deepcuts_api import DeepcutsApi  # noqa: E501


class TestDeepcutsApi(unittest.TestCase):
    """DeepcutsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DeepcutsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_deepcuts_get_albums_by_artist(self) -> None:
        """Test case for deepcuts_get_albums_by_artist

        Get Albums By Artist  # noqa: E501
        """

    def test_deepcuts_recommend_albums_from_albums(self) -> None:
        """Test case for deepcuts_recommend_albums_from_albums

        Recommend Albums From Albums  # noqa: E501
        """


if __name__ == "__main__":
    unittest.main()
