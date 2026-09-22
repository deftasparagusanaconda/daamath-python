from builtins import int as bigint

int8 = None
int16 = None
int32 = None
int64 = None

class int32:
    @classmethod
    def floor(cls, x):
        match x:
            case int32(): return floor(x)
            case binary64(): return cls(...)
            case _: raise NotImplementedError
