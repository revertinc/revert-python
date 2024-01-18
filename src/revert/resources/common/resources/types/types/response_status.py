# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ResponseStatus(str, enum.Enum):
    OK = "ok"
    ERROR = "error"

    def visit(self, ok: typing.Callable[[], T_Result], error: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseStatus.OK:
            return ok()
        if self is ResponseStatus.ERROR:
            return error()
