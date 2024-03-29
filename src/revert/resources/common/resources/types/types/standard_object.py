# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class StandardObject(str, enum.Enum):
    COMPANY = "company"
    CONTACT = "contact"
    DEAL = "deal"
    EVENT = "event"
    LEAD = "lead"
    NOTE = "note"
    TASK = "task"
    USER = "user"

    def visit(
        self,
        company: typing.Callable[[], T_Result],
        contact: typing.Callable[[], T_Result],
        deal: typing.Callable[[], T_Result],
        event: typing.Callable[[], T_Result],
        lead: typing.Callable[[], T_Result],
        note: typing.Callable[[], T_Result],
        task: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StandardObject.COMPANY:
            return company()
        if self is StandardObject.CONTACT:
            return contact()
        if self is StandardObject.DEAL:
            return deal()
        if self is StandardObject.EVENT:
            return event()
        if self is StandardObject.LEAD:
            return lead()
        if self is StandardObject.NOTE:
            return note()
        if self is StandardObject.TASK:
            return task()
        if self is StandardObject.USER:
            return user()
