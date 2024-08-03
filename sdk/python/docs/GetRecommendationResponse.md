# GetRecommendationResponse

Schema for a recommendation response.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**albums** | [**List[Album]**](Album.md) |  |

## Example

```python
from deepcuts_sdk.models.get_recommendation_response import GetRecommendationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecommendationResponse from a JSON string
get_recommendation_response_instance = GetRecommendationResponse.from_json(json)
# print the JSON string representation of the object
print GetRecommendationResponse.to_json()

# convert the object into a dict
get_recommendation_response_dict = get_recommendation_response_instance.to_dict()
# create an instance of GetRecommendationResponse from a dict
get_recommendation_response_from_dict = GetRecommendationResponse.from_dict(get_recommendation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
