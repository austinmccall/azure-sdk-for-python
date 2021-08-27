# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ...operations._accounts_operations import build_get_access_keys_request, build_get_account_properties_request, build_regenerate_access_key_request, build_update_account_properties_request

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class AccountsOperations:
    """AccountsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get_account_properties(
        self,
        **kwargs: Any
    ) -> Any:
        """Get an account.

        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "id": "str (optional)",
                    "identity": {
                        "principalId": "str (optional)",
                        "tenantId": "str (optional)",
                        "type": "str (optional)"
                    },
                    "location": "str (optional)",
                    "name": "str (optional)",
                    "properties": {
                        "cloudConnectors": {
                            "awsExternalId": "str (optional)"
                        },
                        "createdAt": "datetime (optional)",
                        "createdBy": "str (optional)",
                        "createdByObjectId": "str (optional)",
                        "endpoints": {
                            "catalog": "str (optional)",
                            "guardian": "str (optional)",
                            "scan": "str (optional)"
                        },
                        "friendlyName": "str (optional)",
                        "managedResourceGroupName": "str (optional)",
                        "managedResources": {
                            "eventHubNamespace": "str (optional)",
                            "resourceGroup": "str (optional)",
                            "storageAccount": "str (optional)"
                        },
                        "privateEndpointConnections": [
                            {
                                "id": "str (optional)",
                                "name": "str (optional)",
                                "properties": {
                                    "privateEndpoint": {
                                        "id": "str (optional)"
                                    },
                                    "privateLinkServiceConnectionState": {
                                        "actionsRequired": "str (optional)",
                                        "description": "str (optional)",
                                        "status": "str (optional)"
                                    },
                                    "provisioningState": "str (optional)"
                                },
                                "type": "str (optional)"
                            }
                        ],
                        "provisioningState": "str (optional)",
                        "publicNetworkAccess": "str (optional). Default value is \"Enabled\""
                    },
                    "sku": {
                        "capacity": "int (optional)",
                        "name": "str (optional)"
                    },
                    "systemData": {
                        "createdAt": "datetime (optional)",
                        "createdBy": "str (optional)",
                        "createdByType": "str (optional)",
                        "lastModifiedAt": "datetime (optional)",
                        "lastModifiedBy": "str (optional)",
                        "lastModifiedByType": "str (optional)"
                    },
                    "tags": {
                        "str": "str (optional)"
                    },
                    "type": "str (optional)"
                }
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_account_properties_request(
            template_url=self.get_account_properties.metadata['url'],
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_account_properties.metadata = {'url': '/'}  # type: ignore


    @distributed_trace_async
    async def update_account_properties(
        self,
        account_update_parameters: Any,
        **kwargs: Any
    ) -> Any:
        """Updates an account.

        :param account_update_parameters:
        :type account_update_parameters: Any
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                account_update_parameters = {
                    "friendlyName": "str (optional)"
                }

                # response body for status code(s): 200
                response.json() == {
                    "id": "str (optional)",
                    "identity": {
                        "principalId": "str (optional)",
                        "tenantId": "str (optional)",
                        "type": "str (optional)"
                    },
                    "location": "str (optional)",
                    "name": "str (optional)",
                    "properties": {
                        "cloudConnectors": {
                            "awsExternalId": "str (optional)"
                        },
                        "createdAt": "datetime (optional)",
                        "createdBy": "str (optional)",
                        "createdByObjectId": "str (optional)",
                        "endpoints": {
                            "catalog": "str (optional)",
                            "guardian": "str (optional)",
                            "scan": "str (optional)"
                        },
                        "friendlyName": "str (optional)",
                        "managedResourceGroupName": "str (optional)",
                        "managedResources": {
                            "eventHubNamespace": "str (optional)",
                            "resourceGroup": "str (optional)",
                            "storageAccount": "str (optional)"
                        },
                        "privateEndpointConnections": [
                            {
                                "id": "str (optional)",
                                "name": "str (optional)",
                                "properties": {
                                    "privateEndpoint": {
                                        "id": "str (optional)"
                                    },
                                    "privateLinkServiceConnectionState": {
                                        "actionsRequired": "str (optional)",
                                        "description": "str (optional)",
                                        "status": "str (optional)"
                                    },
                                    "provisioningState": "str (optional)"
                                },
                                "type": "str (optional)"
                            }
                        ],
                        "provisioningState": "str (optional)",
                        "publicNetworkAccess": "str (optional). Default value is \"Enabled\""
                    },
                    "sku": {
                        "capacity": "int (optional)",
                        "name": "str (optional)"
                    },
                    "systemData": {
                        "createdAt": "datetime (optional)",
                        "createdBy": "str (optional)",
                        "createdByType": "str (optional)",
                        "lastModifiedAt": "datetime (optional)",
                        "lastModifiedBy": "str (optional)",
                        "lastModifiedByType": "str (optional)"
                    },
                    "tags": {
                        "str": "str (optional)"
                    },
                    "type": "str (optional)"
                }
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        json = account_update_parameters

        request = build_update_account_properties_request(
            content_type=content_type,
            json=json,
            template_url=self.update_account_properties.metadata['url'],
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update_account_properties.metadata = {'url': '/'}  # type: ignore


    @distributed_trace_async
    async def get_access_keys(
        self,
        **kwargs: Any
    ) -> Any:
        """List the authorization keys associated with this account.

        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "atlasKafkaPrimaryEndpoint": "str (optional)",
                    "atlasKafkaSecondaryEndpoint": "str (optional)"
                }
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_access_keys_request(
            template_url=self.get_access_keys.metadata['url'],
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_access_keys.metadata = {'url': '/listkeys'}  # type: ignore


    @distributed_trace_async
    async def regenerate_access_key(
        self,
        key_options: Any,
        **kwargs: Any
    ) -> Any:
        """Regenerate the authorization keys associated with this data catalog.

        :param key_options:
        :type key_options: Any
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                key_options = {
                    "keyType": "str (optional)"
                }

                # response body for status code(s): 200
                response.json() == {
                    "atlasKafkaPrimaryEndpoint": "str (optional)",
                    "atlasKafkaSecondaryEndpoint": "str (optional)"
                }
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        json = key_options

        request = build_regenerate_access_key_request(
            content_type=content_type,
            json=json,
            template_url=self.regenerate_access_key.metadata['url'],
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    regenerate_access_key.metadata = {'url': '/regeneratekeys'}  # type: ignore
