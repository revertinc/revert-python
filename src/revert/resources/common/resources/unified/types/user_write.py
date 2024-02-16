# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class UserWrite(pydantic.BaseModel):
    """
    Include the "businessUnitId" in the "additional" section, as it is a mandatory field for Microsoft Dynamics Sales.
    """

    first_name: str = pydantic.Field(alias="firstName", description="The first name of a user in a CRM.")
    last_name: str = pydantic.Field(alias="lastName", description="The last name of a user in a CRM.")
    phone: str = pydantic.Field(description="The phone number of a user in a CRM.")
    email: str = pydantic.Field(description="The email of a user in a CRM.")

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
