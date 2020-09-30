# swagger_client.SystemApi

All URIs are relative to *{protocol}://{ip}/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_config_get**](SystemApi.md#system_config_get) | **GET** /System/config | get the configuration
[**system_config_post**](SystemApi.md#system_config_post) | **POST** /System/config | set the configuration
[**system_reboot_post**](SystemApi.md#system_reboot_post) | **POST** /System/reboot | reboots the System

# **system_config_get**
> SystemConfig system_config_get()

get the configuration

returns current conffiguration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()

try:
    # get the configuration
    api_response = api_instance.system_config_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_config_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemConfig**](SystemConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_config_post**
> SystemConfig system_config_post()

set the configuration

returns current configuration if accepted

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()

try:
    # set the configuration
    api_response = api_instance.system_config_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_config_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemConfig**](SystemConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_reboot_post**
> SystemConfig system_reboot_post()

reboots the System

returns current configuration if accepted

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()

try:
    # reboots the System
    api_response = api_instance.system_reboot_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_reboot_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemConfig**](SystemConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

