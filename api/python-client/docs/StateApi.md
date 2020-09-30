# swagger_client.StateApi

All URIs are relative to *{protocol}://{ip}/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**state_side_get**](StateApi.md#state_side_get) | **GET** /state/side | get the current CubeState
[**state_system_get**](StateApi.md#state_system_get) | **GET** /state/System | get the current SystemState

# **state_side_get**
> CubeState state_side_get()

get the current CubeState

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StateApi()

try:
    # get the current CubeState
    api_response = api_instance.state_side_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateApi->state_side_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CubeState**](CubeState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **state_system_get**
> SystemState state_system_get()

get the current SystemState

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StateApi()

try:
    # get the current SystemState
    api_response = api_instance.state_system_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateApi->state_system_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemState**](SystemState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

