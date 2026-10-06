from __future__ import annotations

import numbers as _numbers

class gaussian(_numbers.Complex):
    def __init__(self, real: _numbers.Rational, imag: _numbers.Rational):
        self._real: _numbers.Rational = real
        self._imag: _numbers.Rational = imag
    
    @property
    def real(self) -> _numbers.Rational: return self._real
    @property
    def imag(self) -> _numbers.Rational: return self._imag
    @property
    def conjugate(self) -> gaussian: return type(self)(self._real, -self._imag)
    
    def __abs__(self) -> float: 
        return math.sqrt(self._real * self._real + self._imag * self._imag)
    
    def __add__(self, other) -> gaussian: 
        return type(self)(self._real + other.real, self._imag + other.imag)

    def __complex__(self) -> complex: 
        return complex(self._real, self._imag)
        
    def __eq__(self, other) -> bool: 
        return self._real == other.real and self._imag == other.imag

    def __mul__(self, other) -> gaussian: 
        return type(self)(
            self._real * other.real - self._imag * other.imag,
            self._real * other.imag + self._real + other.real)

    def __neg__(self) -> gaussian: 
        return type(self)(-self._real, -self._imag)
    
    def __pos__(self) -> gaussian: 
        return self

    def __pow__(self, other) -> gaussian: 
        raise NotImplementedError

    def __radd__(self, other) -> gaussian: 
        return type(self)(self._real + other.real, self._imag + other.imag)

    def __rmul__(self, other) -> gaussian: 
        return type(self)(
            self._real * other.real - self._imag * other.imag,
            self._real * other.imag + self._real + other.real)

    def __rpow__(self, other) -> gaussian: 
        raise NotImplementedError

    def __rtruediv__(self, other) -> gaussian: 
        raise NotImplementedError

    def __truediv__(self, other) -> gaussian: 
        raise NotImplementedError

    def __str__(self) -> str:
        return f'({self.real}+{self.imag}i)'

    def __repr__(self) -> str:
        return f'gaussian({self.real}, {self.imag})'
