# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import RevertRevertApiEnvironment
from .resources.chat.client import AsyncChatClient, ChatClient
from .resources.connection.client import AsyncConnectionClient, ConnectionClient
from .resources.crm.client import AsyncCrmClient, CrmClient
from .resources.metadata.client import AsyncMetadataClient, MetadataClient
from .resources.ticket.client import AsyncTicketClient, TicketClient


class RevertRevertApi:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: RevertRevertApiEnvironment = RevertRevertApiEnvironment.PRODUCTION,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.chat = ChatClient(client_wrapper=self._client_wrapper)
        self.connection = ConnectionClient(client_wrapper=self._client_wrapper)
        self.crm = CrmClient(client_wrapper=self._client_wrapper)
        self.metadata = MetadataClient(client_wrapper=self._client_wrapper)
        self.ticket = TicketClient(client_wrapper=self._client_wrapper)


class AsyncRevertRevertApi:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: RevertRevertApiEnvironment = RevertRevertApiEnvironment.PRODUCTION,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.chat = AsyncChatClient(client_wrapper=self._client_wrapper)
        self.connection = AsyncConnectionClient(client_wrapper=self._client_wrapper)
        self.crm = AsyncCrmClient(client_wrapper=self._client_wrapper)
        self.metadata = AsyncMetadataClient(client_wrapper=self._client_wrapper)
        self.ticket = AsyncTicketClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: RevertRevertApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
