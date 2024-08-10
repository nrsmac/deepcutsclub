# deepcuts_sdk.DeepcutsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deepcuts_get_albums_by_artist**](DeepcutsApi.md#deepcuts_get_albums_by_artist) | **GET** /albums/{artist_name} | Get Albums By Artist
[**deepcuts_recommend_albums_from_albums**](DeepcutsApi.md#deepcuts_recommend_albums_from_albums) | **POST** /recommend | Recommend Albums From Albums


# **deepcuts_get_albums_by_artist**
> GetArtistAlbumsResponse deepcuts_get_albums_by_artist(artist_name)

Get Albums By Artist

Get albums by artist name.

### Example

```python
import time
import os
import deepcuts_sdk
from deepcuts_sdk.models.get_artist_albums_response import GetArtistAlbumsResponse
from deepcuts_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = deepcuts_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with deepcuts_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepcuts_sdk.DeepcutsApi(api_client)
    artist_name = 'artist_name_example' # str |

    try:
        # Get Albums By Artist
        api_response = api_instance.deepcuts_get_albums_by_artist(artist_name)
        print("The response of DeepcutsApi->deepcuts_get_albums_by_artist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeepcutsApi->deepcuts_get_albums_by_artist: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artist_name** | **str**|  |

### Return type

[**GetArtistAlbumsResponse**](GetArtistAlbumsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deepcuts_recommend_albums_from_albums**
> GetRecommendationResponse deepcuts_recommend_albums_from_albums(body_deepcuts_recommend_albums_from_albums)

Recommend Albums From Albums

Recommend albums based on shared artists.

### Example

```python
import time
import os
import deepcuts_sdk
from deepcuts_sdk.models.body_deepcuts_recommend_albums_from_albums import BodyDeepcutsRecommendAlbumsFromAlbums
from deepcuts_sdk.models.get_recommendation_response import GetRecommendationResponse
from deepcuts_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = deepcuts_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with deepcuts_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepcuts_sdk.DeepcutsApi(api_client)
    body_deepcuts_recommend_albums_from_albums = deepcuts_sdk.BodyDeepcutsRecommendAlbumsFromAlbums() # BodyDeepcutsRecommendAlbumsFromAlbums |

    try:
        # Recommend Albums From Albums
        api_response = api_instance.deepcuts_recommend_albums_from_albums(body_deepcuts_recommend_albums_from_albums)
        print("The response of DeepcutsApi->deepcuts_recommend_albums_from_albums:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeepcutsApi->deepcuts_recommend_albums_from_albums: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_deepcuts_recommend_albums_from_albums** | [**BodyDeepcutsRecommendAlbumsFromAlbums**](BodyDeepcutsRecommendAlbumsFromAlbums.md)|  |

### Return type

[**GetRecommendationResponse**](GetRecommendationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
