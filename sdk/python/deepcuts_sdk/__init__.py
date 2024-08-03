# coding: utf-8

# flake8: noqa

"""
    Deepcuts API

    An API to access music artist metadata and recommendations.

    The version of the OpenAPI document: v0.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from deepcuts_sdk.api.deepcuts_api import DeepcutsApi
from deepcuts_sdk.api_client import ApiClient

# import ApiClient
from deepcuts_sdk.api_response import ApiResponse
from deepcuts_sdk.configuration import Configuration
from deepcuts_sdk.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)

# import models into sdk package
from deepcuts_sdk.models.album import Album
from deepcuts_sdk.models.body_deepcuts_recommend_albums_from_albums import BodyDeepcutsRecommendAlbumsFromAlbums
from deepcuts_sdk.models.genre import Genre
from deepcuts_sdk.models.get_artist_albums_response import GetArtistAlbumsResponse
from deepcuts_sdk.models.get_recommendation_response import GetRecommendationResponse
from deepcuts_sdk.models.http_validation_error import HTTPValidationError
from deepcuts_sdk.models.validation_error import ValidationError
from deepcuts_sdk.models.validation_error_loc_inner import ValidationErrorLocInner
