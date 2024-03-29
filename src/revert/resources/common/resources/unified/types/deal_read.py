# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DealRead(pydantic.BaseModel):
    amount: int = pydantic.Field(description="The deal amount mentioned in the CRM for this deal.")
    priority: typing.Optional[str] = pydantic.Field(
        description="The priority attached to this deal. (not supported by pipedrive)"
    )
    stage: str = pydantic.Field(description="Deal stage in the CRM.")
    name: str = pydantic.Field(description="The name of the deal in a CRM.")
    expected_close_date: typing.Any = pydantic.Field(
        alias="expectedCloseDate",
        description="Expected close date for this deal. (not supported by pipedrive search api)",
    )
    is_won: bool = pydantic.Field(alias="isWon", description="Is `true` if the deal is closed (won).")
    probability: int = pydantic.Field(
        description="Probability of the deal getting closed, a decimal number between 0 to 1 (inclusive)."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
