# BodyDeepcutsRecommendAlbumsFromAlbums


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**album_titles** | **List[str]** |  |
**artist_names** | **List[str]** |  |
**genres** | [**List[Genre]**](Genre.md) |  | [optional]

## Example

```python
from deepcuts_sdk.models.body_deepcuts_recommend_albums_from_albums import BodyDeepcutsRecommendAlbumsFromAlbums

# TODO update the JSON string below
json = "{}"
# create an instance of BodyDeepcutsRecommendAlbumsFromAlbums from a JSON string
body_deepcuts_recommend_albums_from_albums_instance = BodyDeepcutsRecommendAlbumsFromAlbums.from_json(json)
# print the JSON string representation of the object
print BodyDeepcutsRecommendAlbumsFromAlbums.to_json()

# convert the object into a dict
body_deepcuts_recommend_albums_from_albums_dict = body_deepcuts_recommend_albums_from_albums_instance.to_dict()
# create an instance of BodyDeepcutsRecommendAlbumsFromAlbums from a dict
body_deepcuts_recommend_albums_from_albums_from_dict = BodyDeepcutsRecommendAlbumsFromAlbums.from_dict(body_deepcuts_recommend_albums_from_albums_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
