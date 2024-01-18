# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from ....common.resources.errors.errors.internal_server_error import InternalServerError
from ....common.resources.errors.errors.not_found_error import NotFoundError
from ....common.resources.errors.errors.un_authorized_error import UnAuthorizedError
from ....common.resources.errors.types.base_error import BaseError
from .types.create_or_update_deal_request import CreateOrUpdateDealRequest
from .types.create_or_update_deal_response import CreateOrUpdateDealResponse
from .types.get_deal_response import GetDealResponse
from .types.get_deals_response import GetDealsResponse
from .types.search_deals_response import SearchDealsResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DealClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_deal(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> GetDealResponse:
        """
        Get details of a deal

        Parameters:
            - id: str.

            - fields: typing.Optional[str].

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"crm/deals/{id}"),
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
            return pydantic.parse_obj_as(GetDealResponse, _response.json())  # type: ignore
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

    def get_deals(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> GetDealsResponse:
        """
        Get all the deals

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
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "crm/deals"),
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
            return pydantic.parse_obj_as(GetDealsResponse, _response.json())  # type: ignore
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

    def create_deal(
        self,
        *,
        request: CreateOrUpdateDealRequest,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> CreateOrUpdateDealResponse:
        """
        Create a new deal

        Parameters:
            - request: CreateOrUpdateDealRequest.

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "crm/deals"),
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
            return pydantic.parse_obj_as(CreateOrUpdateDealResponse, _response.json())  # type: ignore
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

    def update_deal(
        self,
        id: str,
        *,
        request: CreateOrUpdateDealRequest,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> CreateOrUpdateDealResponse:
        """
        Update a deal

        Parameters:
            - id: str.

            - request: CreateOrUpdateDealRequest.

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"crm/deals/{id}"),
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
            return pydantic.parse_obj_as(CreateOrUpdateDealResponse, _response.json())  # type: ignore
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

    def search_deals(
        self,
        *,
        fields: typing.Optional[str] = None,
        search_criteria: typing.Any,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> SearchDealsResponse:
        """
        Search for deals

        Parameters:
            - fields: typing.Optional[str].

            - search_criteria: typing.Any.

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "crm/deals/search"),
            params=remove_none_from_dict({"fields": fields}),
            json=jsonable_encoder({"searchCriteria": search_criteria}),
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
            return pydantic.parse_obj_as(SearchDealsResponse, _response.json())  # type: ignore
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


class AsyncDealClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_deal(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> GetDealResponse:
        """
        Get details of a deal

        Parameters:
            - id: str.

            - fields: typing.Optional[str].

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"crm/deals/{id}"),
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
            return pydantic.parse_obj_as(GetDealResponse, _response.json())  # type: ignore
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

    async def get_deals(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> GetDealsResponse:
        """
        Get all the deals

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
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "crm/deals"),
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
            return pydantic.parse_obj_as(GetDealsResponse, _response.json())  # type: ignore
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

    async def create_deal(
        self,
        *,
        request: CreateOrUpdateDealRequest,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> CreateOrUpdateDealResponse:
        """
        Create a new deal

        Parameters:
            - request: CreateOrUpdateDealRequest.

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "crm/deals"),
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
            return pydantic.parse_obj_as(CreateOrUpdateDealResponse, _response.json())  # type: ignore
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

    async def update_deal(
        self,
        id: str,
        *,
        request: CreateOrUpdateDealRequest,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> CreateOrUpdateDealResponse:
        """
        Update a deal

        Parameters:
            - id: str.

            - request: CreateOrUpdateDealRequest.

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"crm/deals/{id}"),
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
            return pydantic.parse_obj_as(CreateOrUpdateDealResponse, _response.json())  # type: ignore
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

    async def search_deals(
        self,
        *,
        fields: typing.Optional[str] = None,
        search_criteria: typing.Any,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> SearchDealsResponse:
        """
        Search for deals

        Parameters:
            - fields: typing.Optional[str].

            - search_criteria: typing.Any.

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "crm/deals/search"),
            params=remove_none_from_dict({"fields": fields}),
            json=jsonable_encoder({"searchCriteria": search_criteria}),
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
            return pydantic.parse_obj_as(SearchDealsResponse, _response.json())  # type: ignore
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