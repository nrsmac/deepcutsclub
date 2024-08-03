# GetArtistAlbumsResponse

Schema for an album_response.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**albums** | [**List[Album]**](Album.md) |  |

## Example

```python
from deepcuts_sdk.models.get_artist_albums_response import GetArtistAlbumsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetArtistAlbumsResponse from a JSON string
get_artist_albums_response_instance = GetArtistAlbumsResponse.from_json(json)
# print the JSON string representation of the object
print GetArtistAlbumsResponse.to_json()

# convert the object into a dict
get_artist_albums_response_dict = get_artist_albums_response_instance.to_dict()
# create an instance of GetArtistAlbumsResponse from a dict
get_artist_albums_response_from_dict = GetArtistAlbumsResponse.from_dict(get_artist_albums_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
