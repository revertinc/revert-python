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


class Connection(pydantic.BaseModel):
    tp_id: Tpid
    tp_access_token: str
    tp_refresh_token: typing.Optional[str]
    tp_customer_id: str
    t_id: str
    tp_account_url: typing.Optional[str]
    owner_account_public_token: str
    app_client_id: typing.Optional[str]
    app_client_secret: typing.Optional[str]
    app: typing.Optional[App]

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


from .app import App  # noqa: E402

Connection.update_forward_refs()
