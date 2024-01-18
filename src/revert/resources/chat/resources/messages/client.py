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
from .types.createor_update_message_request import CreateorUpdateMessageRequest
from .types.createor_update_message_response import CreateorUpdateMessageResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class MessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_message(
        self,
        *,
        request: CreateorUpdateMessageRequest,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> CreateorUpdateMessageResponse:
        """
        Create a new message

        Parameters:
            - request: CreateorUpdateMessageRequest.

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "chat/message"),
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
            return pydantic.parse_obj_as(CreateorUpdateMessageResponse, _response.json())  # type: ignore
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


class AsyncMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_message(
        self,
        *,
        request: CreateorUpdateMessageRequest,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> CreateorUpdateMessageResponse:
        """
        Create a new message

        Parameters:
            - request: CreateorUpdateMessageRequest.

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "chat/message"),
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
            return pydantic.parse_obj_as(CreateorUpdateMessageResponse, _response.json())  # type: ignore
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
