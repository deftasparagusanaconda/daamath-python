from numbers import Integral as _Integral
import math as _math

class ClosureError(Exception):
    ...

class uint(_Integral):
    def __init__(self, value: _Integral):
        if not isinstance(value, _Integral):
            raise TypeError(f'not isinstance({value=}, numbers.Integral)')
        if value < 0:
            raise ValueError(f'{value=} < 0')
        self.value: _Integral = value

    def __pos__(self): return self
    def __neg__(self): 
        if self.value == 0:
            return self
        else:
            raise ValueError('naturals are not closed under negation')
    def __abs__(self): return self
    def __floor__(self): return self
    def __ceil__(self): return self
    def __trunc__(self): return self
    def __round__(self, ndigits=None): return self
    def __add__(self, other): return type(self)(self.value + other.value)
    def __radd__(self, other): return type(self)(self.value + other.value)
    def __sub__(self, other): return type(self)(self.value - other.value)
    def __mul__(self, other): return type(self)(self.value * other.value)
    def __rmul__(self, other): return type(self)(self.value * other.value)
    def __pow__(self, other): return type(self)(self.value ** other.value)
    def __rpow__(self, other): return type(self)(self.value ** other.value)
    def __truediv__(self, other): 
        if self.value % other.value != 0:
            raise ValueError(f'{self.value=} % {other.value=} != 0')
        return type(self)(self.value // other.value)
    def __rtruediv__(self, other): 
        return self / other
    def __floordiv__(self, other): return type(self)(self.value // other.value)
    def __rfloordiv__(self, other): return type(self)(self.value // other.value)
    def __mod__(self, other): return type(self)(self.value % other.value)
    def __rmod__(self, other): return type(self)(self.value % other.value)
    def __le__(self, other): return self.value <= other.value
    def __eq__(self, other): return self.value == other.value
    def __lt__(self, other): return self.value < other.value
    def __invert__(self): raise NotImplemented
    def __and__(self, other): raise NotImplemented
    def __rand__(self, other): raise NotImplemented
    def __or__(self, other): raise NotImplemented
    def __ror__(self, other): raise NotImplemented
    def __xor__(self, other): raise NotImplemented
    def __rxor__(self, other): raise NotImplemented
    def __lshift__(self, other): raise NotImplemented
    def __rlshift__(self, other): raise NotImplemented
    def __rshift__(self, other): raise NotImplemented
    def __rrshift__(self, other): raise NotImplemented
    def __int__(self) -> int: return int(self.value)

    def __log__(self, other): ...
    def __root__(self, other): ...
    def __min__(self, other): return type(self)(min(self.value, other.value))
    def __max__(self, other): return type(self)(max(self.value, other.value))
    def __gcd__(self, other): return type(self)(_math.gcd(self.value, other.value))
    def __lcm__(self, other): return type(self)(_math.lcm(self.value, other.value))
    
    def __str__(self): return str(self.value)

class biguint(uint):
    ...

class uint8(uint):
    def __init__(self, value: _Integral):
        if not 0 <= value < 2 ** 8:
            raise ValueError(f'not 0 <= {value=} < 2 ** 8')        
        super().__init__(value)

class uint16(uint):
    def __init__(self, value: _Integral):
        if not 0 <= value < 2 ** 16:
            raise ValueError(f'not 0 <= {value=} < 2 ** 16')        
        super().__init__(value)

class uint32(uint):
    def __init__(self, value: _Integral):
        if not 0 <= value < 2 ** 32:
            raise ValueError(f'not 0 <= {value=} < 2 ** 32')        
        super().__init__(value)

class uint64(uint):
    def __init__(self, value: _Integral):
        if not 0 <= value < 2 ** 64:
            raise ValueError(f'not 0 <= {value=} < 2 ** 64')
        super().__init__(value)
