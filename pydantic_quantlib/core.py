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
            return ql_obj(*filter(None, args))

        attr = getattr(self, field)
        if isinstance(attr, BaseModel):
            return attr.to_quantlib()
        if isinstance(attr, Enum):
            return attr.value

        return attr
