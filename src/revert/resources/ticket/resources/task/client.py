# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from ....common.resources.errors.errors.bad_request_error import BadRequestError
from ....common.resources.errors.errors.internal_server_error import InternalServerError
from ....common.resources.errors.errors.not_found_error import NotFoundError
from ....common.resources.errors.errors.un_authorized_error import UnAuthorizedError
from ....common.resources.errors.types.base_error import BaseError
from .types.create_or_update_task_request import CreateOrUpdateTaskRequest
from .types.create_or_update_task_response import CreateOrUpdateTaskResponse
from .types.get_task_response import GetTaskResponse
from .types.get_tasks_response import GetTasksResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TaskClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_task(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> GetTaskResponse:
        """
        Get details of a task

        Parameters:
            - id: str.

            - fields: typing.Optional[str].

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"ticket/tasks/{id}"),
            params=remove_none_from_dict({"fields": fields}),
            headers=remove_none_from_dict(
                {
                    **self._client_wrapper.get_headers(),
                    "x-revert-api-token": x_revert_api_token,
                    "x-revert-t-id": x_revert_t_id,
                    "x-api-version": x_api_version,
                }
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetTaskResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnAuthorizedError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_tasks(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> GetTasksResponse:
        """
        Get all the tasks

        Parameters:
            - fields: typing.Optional[str].

            - page_size: typing.Optional[str].

            - cursor: typing.Optional[str].

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "ticket/tasks"),
            params=remove_none_from_dict({"fields": fields, "pageSize": page_size, "cursor": cursor}),
            headers=remove_none_from_dict(
                {
                    **self._client_wrapper.get_headers(),
                    "x-revert-api-token": x_revert_api_token,
                    "x-revert-t-id": x_revert_t_id,
                    "x-api-version": x_api_version,
                }
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetTasksResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnAuthorizedError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_task(
        self,
        *,
        request: CreateOrUpdateTaskRequest,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> CreateOrUpdateTaskResponse:
        """
        Parameters:
            - request: CreateOrUpdateTaskRequest.

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "ticket/tasks"),
            json=jsonable_encoder(request),
            headers=remove_none_from_dict(
                {
                    **self._client_wrapper.get_headers(),
                    "x-revert-api-token": x_revert_api_token,
                    "x-revert-t-id": x_revert_t_id,
                    "x-api-version": x_api_version,
                }
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateOrUpdateTaskResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnAuthorizedError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_task(
        self,
        id: str,
        *,
        request: CreateOrUpdateTaskRequest,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> CreateOrUpdateTaskResponse:
        """
        Update a task

        Parameters:
            - id: str.

            - request: CreateOrUpdateTaskRequest.

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"ticket/tasks/{id}"),
            json=jsonable_encoder(request),
            headers=remove_none_from_dict(
                {
                    **self._client_wrapper.get_headers(),
                    "x-revert-api-token": x_revert_api_token,
                    "x-revert-t-id": x_revert_t_id,
                    "x-api-version": x_api_version,
                }
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateOrUpdateTaskResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnAuthorizedError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTaskClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_task(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> GetTaskResponse:
        """
        Get details of a task

        Parameters:
            - id: str.

            - fields: typing.Optional[str].

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"ticket/tasks/{id}"),
            params=remove_none_from_dict({"fields": fields}),
            headers=remove_none_from_dict(
                {
                    **self._client_wrapper.get_headers(),
                    "x-revert-api-token": x_revert_api_token,
                    "x-revert-t-id": x_revert_t_id,
                    "x-api-version": x_api_version,
                }
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetTaskResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnAuthorizedError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_tasks(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> GetTasksResponse:
        """
        Get all the tasks

        Parameters:
            - fields: typing.Optional[str].

            - page_size: typing.Optional[str].

            - cursor: typing.Optional[str].

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "ticket/tasks"),
            params=remove_none_from_dict({"fields": fields, "pageSize": page_size, "cursor": cursor}),
            headers=remove_none_from_dict(
                {
                    **self._client_wrapper.get_headers(),
                    "x-revert-api-token": x_revert_api_token,
                    "x-revert-t-id": x_revert_t_id,
                    "x-api-version": x_api_version,
                }
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetTasksResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnAuthorizedError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_task(
        self,
        *,
        request: CreateOrUpdateTaskRequest,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> CreateOrUpdateTaskResponse:
        """
        Parameters:
            - request: CreateOrUpdateTaskRequest.

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "ticket/tasks"),
            json=jsonable_encoder(request),
            headers=remove_none_from_dict(
                {
                    **self._client_wrapper.get_headers(),
                    "x-revert-api-token": x_revert_api_token,
                    "x-revert-t-id": x_revert_t_id,
                    "x-api-version": x_api_version,
                }
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateOrUpdateTaskResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnAuthorizedError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_task(
        self,
        id: str,
        *,
        request: CreateOrUpdateTaskRequest,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> CreateOrUpdateTaskResponse:
        """
        Update a task

        Parameters:
            - id: str.

            - request: CreateOrUpdateTaskRequest.

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"ticket/tasks/{id}"),
            json=jsonable_encoder(request),
            headers=remove_none_from_dict(
                {
                    **self._client_wrapper.get_headers(),
                    "x-revert-api-token": x_revert_api_token,
                    "x-revert-t-id": x_revert_t_id,
                    "x-api-version": x_api_version,
                }
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateOrUpdateTaskResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnAuthorizedError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(BaseError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
