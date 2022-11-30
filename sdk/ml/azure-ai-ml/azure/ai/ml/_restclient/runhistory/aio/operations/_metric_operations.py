# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar, Union

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._metric_operations import build_delete_metrics_by_data_container_id_request_initial, build_delete_metrics_by_run_id_request_initial, build_get_full_fidelity_metric_request, build_get_sampled_metric_request, build_list_generic_resource_metrics_request, build_list_metric_request, build_post_run_metrics_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class MetricOperations:
    """MetricOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.machinelearningservices.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get_full_fidelity_metric(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        run_id: str,
        body: Optional["_models.RetrieveFullFidelityMetricRequest"] = None,
        **kwargs: Any
    ) -> "_models.MetricV2":
        """API to retrieve the full-fidelity sequence associated with a particular run and metricName.

        API to retrieve the full-fidelity sequence associated with a particular run and metricName.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param run_id:
        :type run_id: str
        :param body:
        :type body: ~azure.mgmt.machinelearningservices.models.RetrieveFullFidelityMetricRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MetricV2, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.MetricV2
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.MetricV2"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if body is not None:
            _json = self._serialize.body(body, 'RetrieveFullFidelityMetricRequest')
        else:
            _json = None

        request = build_get_full_fidelity_metric_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            run_id=run_id,
            content_type=content_type,
            json=_json,
            template_url=self.get_full_fidelity_metric.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MetricV2', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_full_fidelity_metric.metadata = {'url': "/metric/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/runs/{runId}/full"}  # type: ignore


    @distributed_trace
    def list_metric(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        run_id: str,
        body: Optional["_models.ListMetrics"] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.PaginatedMetricDefinitionList"]:
        """API to list metric for a particular datacontainer and metricName.

        API to list metric for a particular datacontainer and metricName.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param run_id:
        :type run_id: str
        :param body:
        :type body: ~azure.mgmt.machinelearningservices.models.ListMetrics
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PaginatedMetricDefinitionList or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.machinelearningservices.models.PaginatedMetricDefinitionList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PaginatedMetricDefinitionList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                if body is not None:
                    _json = self._serialize.body(body, 'ListMetrics')
                else:
                    _json = None
                
                request = build_list_metric_request(
                    subscription_id=subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    run_id=run_id,
                    content_type=content_type,
                    json=_json,
                    template_url=self.list_metric.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                if body is not None:
                    _json = self._serialize.body(body, 'ListMetrics')
                else:
                    _json = None
                
                request = build_list_metric_request(
                    subscription_id=subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    run_id=run_id,
                    content_type=content_type,
                    json=_json,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PaginatedMetricDefinitionList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_metric.metadata = {'url': "/metric/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/runs/{runId}/list"}  # type: ignore

    @distributed_trace
    def list_generic_resource_metrics(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        body: Optional["_models.ListGenericResourceMetrics"] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.PaginatedMetricDefinitionList"]:
        """API to list workspace/subworkspace resource metrics for a particular ResourceId.

        API to list workspace/subworkspace resource metrics for a particular ResourceId.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param body:
        :type body: ~azure.mgmt.machinelearningservices.models.ListGenericResourceMetrics
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PaginatedMetricDefinitionList or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.machinelearningservices.models.PaginatedMetricDefinitionList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PaginatedMetricDefinitionList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                if body is not None:
                    _json = self._serialize.body(body, 'ListGenericResourceMetrics')
                else:
                    _json = None
                
                request = build_list_generic_resource_metrics_request(
                    subscription_id=subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    content_type=content_type,
                    json=_json,
                    template_url=self.list_generic_resource_metrics.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                if body is not None:
                    _json = self._serialize.body(body, 'ListGenericResourceMetrics')
                else:
                    _json = None
                
                request = build_list_generic_resource_metrics_request(
                    subscription_id=subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    content_type=content_type,
                    json=_json,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PaginatedMetricDefinitionList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_generic_resource_metrics.metadata = {'url': "/metric/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/azuremonitor/list"}  # type: ignore

    @distributed_trace_async
    async def get_sampled_metric(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        run_id: str,
        body: Optional["_models.GetSampledMetricRequest"] = None,
        **kwargs: Any
    ) -> "_models.MetricSample":
        """Stub for future action
        API to retrieve samples for one or many runs to compare a given metricName
        Throw if schemas don't match across metrics.

        Stub for future action
        API to retrieve samples for one or many runs to compare a given metricName
        Throw if schemas don't match across metrics.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param run_id:
        :type run_id: str
        :param body:
        :type body: ~azure.mgmt.machinelearningservices.models.GetSampledMetricRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MetricSample, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.MetricSample
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.MetricSample"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if body is not None:
            _json = self._serialize.body(body, 'GetSampledMetricRequest')
        else:
            _json = None

        request = build_get_sampled_metric_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            run_id=run_id,
            content_type=content_type,
            json=_json,
            template_url=self.get_sampled_metric.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MetricSample', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_sampled_metric.metadata = {'url': "/metric/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/runs/{runId}/sample"}  # type: ignore


    @distributed_trace_async
    async def post_run_metrics(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        run_id: str,
        body: Optional["_models.BatchIMetricV2"] = None,
        **kwargs: Any
    ) -> "_models.PostRunMetricsResult":
        """Post Metrics to a Run.

        Post Metrics to a specific Run Id.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param run_id:
        :type run_id: str
        :param body:
        :type body: ~azure.mgmt.machinelearningservices.models.BatchIMetricV2
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PostRunMetricsResult, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.PostRunMetricsResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PostRunMetricsResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if body is not None:
            _json = self._serialize.body(body, 'BatchIMetricV2')
        else:
            _json = None

        request = build_post_run_metrics_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            run_id=run_id,
            content_type=content_type,
            json=_json,
            template_url=self.post_run_metrics.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 207]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('PostRunMetricsResult', pipeline_response)

        if response.status_code == 207:
            deserialized = self._deserialize('PostRunMetricsResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    post_run_metrics.metadata = {'url': "/metric/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/runs/{runId}/batch"}  # type: ignore


    async def _delete_metrics_by_data_container_id_initial(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        experiment_id: str,
        data_container_id: str,
        **kwargs: Any
    ) -> Any:
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_metrics_by_data_container_id_request_initial(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            experiment_id=experiment_id,
            data_container_id=data_container_id,
            template_url=self._delete_metrics_by_data_container_id_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('object', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _delete_metrics_by_data_container_id_initial.metadata = {'url': "/metric/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/experiments/{experimentId}/containers/{dataContainerId}/deleteMetrics"}  # type: ignore


    @distributed_trace_async
    async def begin_delete_metrics_by_data_container_id(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        experiment_id: str,
        data_container_id: str,
        **kwargs: Any
    ) -> AsyncLROPoller[Any]:
        """API to delete metrics by data container id.

        API to delete metrics by data container id.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param experiment_id:
        :type experiment_id: str
        :param data_container_id:
        :type data_container_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either any or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[any]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._delete_metrics_by_data_container_id_initial(
                subscription_id=subscription_id,
                resource_group_name=resource_group_name,
                workspace_name=workspace_name,
                experiment_id=experiment_id,
                data_container_id=data_container_id,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('object', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'location'}, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete_metrics_by_data_container_id.metadata = {'url': "/metric/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/experiments/{experimentId}/containers/{dataContainerId}/deleteMetrics"}  # type: ignore

    async def _delete_metrics_by_run_id_initial(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        run_id: str,
        **kwargs: Any
    ) -> Any:
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_metrics_by_run_id_request_initial(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            run_id=run_id,
            template_url=self._delete_metrics_by_run_id_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('object', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _delete_metrics_by_run_id_initial.metadata = {'url': "/metric/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/runs/{runId}/deleteMetrics"}  # type: ignore


    @distributed_trace_async
    async def begin_delete_metrics_by_run_id(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        run_id: str,
        **kwargs: Any
    ) -> AsyncLROPoller[Any]:
        """API to delete metrics by run id.

        API to delete metrics by run id.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param run_id:
        :type run_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either any or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[any]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._delete_metrics_by_run_id_initial(
                subscription_id=subscription_id,
                resource_group_name=resource_group_name,
                workspace_name=workspace_name,
                run_id=run_id,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('object', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'location'}, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete_metrics_by_run_id.metadata = {'url': "/metric/v2.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/runs/{runId}/deleteMetrics"}  # type: ignore

