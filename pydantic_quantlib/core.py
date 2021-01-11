from enum import Enum

import QuantLib as ql
from pydantic import BaseModel as _BaseModel


class BaseModel(_BaseModel):
    class Config:
        extra = "forbid"  # no unexpected fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.to_quantlib()

    def to_quantlib(self, field=None):
        """recover QuantLib object for computation
        >>> from typing import Optional
        >>> class Date(BaseModel):
        ...     resource_name: Optional[str] = "Date"
        ...     d: int
        ...     m: int
        ...     y: int
        >>> date = Date(d=1, m=1, y=2021)
        >>> date.to_quantlib()
        Date(1,1,2021)
        """

        if field is None:  # convert the whole object
            ql_obj = getattr(ql, self.resource_name)
            args = (self.to_quantlib(key) for key, _value in self.__repr_args__())
            args = tuple(arg for arg in args if arg is not None)
            try:
                return ql_obj(*args)
            except Exception as e:
                raise Exception(self.resource_name, args, e)

        attr = getattr(self, field)
        if isinstance(attr, BaseModel):
            # recursively convert the field values
            return attr.to_quantlib()
        if isinstance(attr, Enum):
            # extract integer value of Enum
            return attr.value
        if isinstance(attr, Enum):
            # extract integer value of Enum
            return attr.value

        # else no conversion required
        return attr

    def __repr_args__(self):
        parent = super().__repr_args__()
        return [(key, value) for key, value in parent if key != "resource_name"]
