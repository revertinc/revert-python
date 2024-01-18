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
from .types.create_or_update_lead_request import CreateOrUpdateLeadRequest
from .types.create_or_update_lead_response import CreateOrUpdateLeadResponse
from .types.get_lead_response import GetLeadResponse
from .types.get_leads_response import GetLeadsResponse
from .types.search_leads_response import SearchLeadsResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class LeadClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_lead(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> GetLeadResponse:
        """
        Get details of a lead

        Parameters:
            - id: str.

            - fields: typing.Optional[str].

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"crm/leads/{id}"),
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
            return pydantic.parse_obj_as(GetLeadResponse, _response.json())  # type: ignore
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

    def get_leads(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> GetLeadsResponse:
        """
        Get all the leads

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
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "crm/leads"),
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
            return pydantic.parse_obj_as(GetLeadsResponse, _response.json())  # type: ignore
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

    def create_lead(
        self,
        *,
        request: CreateOrUpdateLeadRequest,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> CreateOrUpdateLeadResponse:
        """
        Create a new lead

        Parameters:
            - request: CreateOrUpdateLeadRequest.

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "crm/leads"),
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
            return pydantic.parse_obj_as(CreateOrUpdateLeadResponse, _response.json())  # type: ignore
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

    def update_lead(
        self,
        id: str,
        *,
        request: CreateOrUpdateLeadRequest,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> CreateOrUpdateLeadResponse:
        """
        Update a lead

        Parameters:
            - id: str.

            - request: CreateOrUpdateLeadRequest.

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"crm/leads/{id}"),
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
            return pydantic.parse_obj_as(CreateOrUpdateLeadResponse, _response.json())  # type: ignore
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

    def search_leads(
        self,
        *,
        fields: typing.Optional[str] = None,
        search_criteria: typing.Any,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> SearchLeadsResponse:
        """
        Search for leads

        Parameters:
            - fields: typing.Optional[str].

            - search_criteria: typing.Any.

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "crm/leads/search"),
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
            return pydantic.parse_obj_as(SearchLeadsResponse, _response.json())  # type: ignore
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


class AsyncLeadClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_lead(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> GetLeadResponse:
        """
        Get details of a lead

        Parameters:
            - id: str.

            - fields: typing.Optional[str].

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"crm/leads/{id}"),
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
            return pydantic.parse_obj_as(GetLeadResponse, _response.json())  # type: ignore
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

    async def get_leads(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> GetLeadsResponse:
        """
        Get all the leads

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
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "crm/leads"),
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
            return pydantic.parse_obj_as(GetLeadsResponse, _response.json())  # type: ignore
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

    async def create_lead(
        self,
        *,
        request: CreateOrUpdateLeadRequest,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> CreateOrUpdateLeadResponse:
        """
        Create a new lead

        Parameters:
            - request: CreateOrUpdateLeadRequest.

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "crm/leads"),
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
            return pydantic.parse_obj_as(CreateOrUpdateLeadResponse, _response.json())  # type: ignore
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

    async def update_lead(
        self,
        id: str,
        *,
        request: CreateOrUpdateLeadRequest,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> CreateOrUpdateLeadResponse:
        """
        Update a lead

        Parameters:
            - id: str.

            - request: CreateOrUpdateLeadRequest.

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"crm/leads/{id}"),
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
            return pydantic.parse_obj_as(CreateOrUpdateLeadResponse, _response.json())  # type: ignore
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

    async def search_leads(
        self,
        *,
        fields: typing.Optional[str] = None,
        search_criteria: typing.Any,
        x_revert_api_token: str,
        x_revert_t_id: str,
        x_api_version: typing.Optional[str] = None,
    ) -> SearchLeadsResponse:
        """
        Search for leads

        Parameters:
            - fields: typing.Optional[str].

            - search_criteria: typing.Any.

            - x_revert_api_token: str. Your official API key for accessing revert apis.

            - x_revert_t_id: str. The unique customer id used when the customer linked their account.

            - x_api_version: typing.Optional[str]. Optional Revert API version you're using. If missing we default to the latest version of the API.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "crm/leads/search"),
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
            return pydantic.parse_obj_as(SearchLeadsResponse, _response.json())  # type: ignore
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
