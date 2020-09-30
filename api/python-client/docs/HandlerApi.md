# swagger_client.HandlerApi

All URIs are relative to *{protocol}://{ip}/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_side_handler**](HandlerApi.md#add_side_handler) | **POST** /handler/side/{sideId} | configures a Handler for side {sideId}
[**handler_onchange_get**](HandlerApi.md#handler_onchange_get) | **GET** /handler/onchange | get the current Handler for changes of CubeState
[**handler_onchange_post**](HandlerApi.md#handler_onchange_post) | **POST** /handler/onchange | configures a Handler for changes of CubeState
[**handler_side_side_id_get**](HandlerApi.md#handler_side_side_id_get) | **GET** /handler/side/{sideId} | get the current Handler for {sideId}

# **add_side_handler**
> Handler add_side_handler(side_id, body=body)

configures a Handler for side {sideId}

Adds a Handler to a side

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HandlerApi()
side_id = swagger_client.SideId() # SideId | 
body = swagger_client.Handler() # Handler |  (optional)

try:
    # configures a Handler for side {sideId}
    api_response = api_instance.add_side_handler(side_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandlerApi->add_side_handler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side_id** | [**SideId**](.md)|  | 
 **body** | [**Handler**](Handler.md)|  | [optional] 

### Return type

[**Handler**](Handler.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handler_onchange_get**
> Handler handler_onchange_get()

get the current Handler for changes of CubeState

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HandlerApi()

try:
    # get the current Handler for changes of CubeState
    api_response = api_instance.handler_onchange_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandlerApi->handler_onchange_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Handler**](Handler.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handler_onchange_post**
> Handler handler_onchange_post(body=body)

configures a Handler for changes of CubeState

Add a Handler to whenever the CubeState changes i.e. it is tilted

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HandlerApi()
body = swagger_client.Handler() # Handler |  (optional)

try:
    # configures a Handler for changes of CubeState
    api_response = api_instance.handler_onchange_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandlerApi->handler_onchange_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Handler**](Handler.md)|  | [optional] 

### Return type

[**Handler**](Handler.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handler_side_side_id_get**
> Handler handler_side_side_id_get(side_id)

get the current Handler for {sideId}

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HandlerApi()
side_id = swagger_client.SideId() # SideId | 

try:
    # get the current Handler for {sideId}
    api_response = api_instance.handler_side_side_id_get(side_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HandlerApi->handler_side_side_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side_id** | [**SideId**](.md)|  | 

### Return type

[**Handler**](Handler.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

