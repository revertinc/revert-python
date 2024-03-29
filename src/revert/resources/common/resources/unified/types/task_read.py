# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TaskRead(pydantic.BaseModel):
    subject: str = pydantic.Field(description="Subject of the task.")
    body: str = pydantic.Field(description="Body of the task description.")
    priority: str = pydantic.Field(description="The priority of the task in hand. (not supported by pipedrive)")
    status: str = pydantic.Field(description="Completion status of the task.")
    due_date: typing.Any = pydantic.Field(alias="dueDate", description="The date when this task is due.")

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
