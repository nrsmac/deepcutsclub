# Album

Schema for an album.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  |
**artist_name** | **str** |  | [optional]
**spotify_id** | **str** |  | [optional]
**spotify_url** | **str** |  | [optional]
**discogs_release_id** | **int** |  | [optional]
**image_url** | **str** |  | [optional]
**credit_artist_ids** | **List[int]** |  | [optional] [default to []]

## Example

```python
from deepcuts_sdk.models.album import Album

# TODO update the JSON string below
json = "{}"
# create an instance of Album from a JSON string
album_instance = Album.from_json(json)
# print the JSON string representation of the object
print Album.to_json()

# convert the object into a dict
album_dict = album_instance.to_dict()
# create an instance of Album from a dict
album_from_dict = Album.from_dict(album_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
