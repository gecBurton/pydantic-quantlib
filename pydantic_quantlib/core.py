from enum import Enum

import QuantLib as ql
from pydantic import BaseModel as _BaseModel


class BaseModel(_BaseModel):
    class Config:
        extra = "forbid"  # no unexpected fields

    def to_quantlib(self, field=None):
        """recover QuantLib object for computation
        >>> class Date(BaseModel):
        ...     d: int
        ...     m: int
        ...     y: int
        >>> date = Date(d=1, m=1, y=2021)
        >>> date.to_quantlib()
        Date(1,1,2021)
        """

        if field is None:  # convert the whole object
            ql_obj = getattr(ql, self.__repr_name__())
            args = (self.to_quantlib(key) for key, _value in self.__repr_args__())
            return ql_obj(*(arg for arg in args if arg is not None))

        attr = getattr(self, field)
        if isinstance(attr, BaseModel):
            # recursively convert the field values
            return attr.to_quantlib()
        if isinstance(attr, Enum):
            # extract integer value of Enum
            return attr.value

        # else no conversion required
        return attr

    def __repr_args__(self):
        parent = super().__repr_args__()
        return [(key, value) for key, value in parent if key != "resource_name"]
