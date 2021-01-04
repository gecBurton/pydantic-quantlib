from enum import Enum

import QuantLib as ql
from pydantic import BaseModel as _BaseModel


class BaseModel(_BaseModel):
    class Config:
        extra = "forbid"

    def to_quantlib(self, field=None):
        if field is None:
            ql_obj = getattr(ql, self.__repr_name__())
            args = (self.to_quantlib(field) for field in self.__fields__)
            args = tuple(arg for arg in args if arg is not None)
            return ql_obj(*args)

        attr = getattr(self, field)
        if isinstance(attr, BaseModel):
            return attr.to_quantlib()
        if isinstance(attr, Enum):
            return attr.value

        schema = self.schema()["properties"][field]
        multiple_of = schema.get("multipleOf")
        if multiple_of == 1:
            return int(attr)
        return attr
