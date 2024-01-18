# This file was auto-generated by Fern from our API Definition.

from ......core.api_error import ApiError
from ..types.base_error import BaseError


class BadRequestError(ApiError):
    def __init__(self, body: BaseError):
        super().__init__(status_code=400, body=body)
