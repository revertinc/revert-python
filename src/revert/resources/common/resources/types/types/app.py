# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime
from .tpid import Tpid

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class App(pydantic.BaseModel):
    id: str
    tp_id: Tpid
    scope: typing.Optional[typing.List[str]]
    app_client_id: typing.Optional[str]
    app_client_secret: typing.Optional[str]
    owner_account_public_token: str
    account: typing.Optional[Account]
    connections: typing.Optional[typing.List[Connection]]
    is_revert_app: bool

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}


from .account import Account  # noqa: E402
from .connection import Connection  # noqa: E402

App.update_forward_refs()
