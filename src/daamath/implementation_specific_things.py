from __future__ import annotations
from numbers import Integral, Rational
from math import gcd, frexp
from fractions import Fraction

class Float(Rational):
    def __init__(self, significand: int, radix: int, exponent: int):
        if significand == 0:
            exponent = 0
        else:
            # canonicalize to reduced form
            while significand % radix == 0:
                significand //= radix
                exponent += 1
        
        self.significand: int = significand
        self.radix: int = radix
        self.exponent: int = exponent
    
    def as_integer_ratio(self) -> tuple[int, int]:
        if self.exponent >= 0:
            numerator = self.significand * self.radix ** self.exponent
            denominator = 1
        else:
            numerator = self.significand
            denominator = self.radix ** -self.exponent

        common = gcd(abs(numerator), denominator)
        return (numerator // common, denominator // common)
    
    @property
    def numerator(self) -> int:
        return self.as_integer_ratio()[0]
    
    @property
    def denominator(self) -> int:
        return self.as_integer_ratio()[1]   
    
    def __int__(self) -> int:
        if self.exponent < 0:
            raise ValueError('this constant cannot be represented as an int')
        return self.significand * self.radix ** self.exponent
        
    def __float__(self) -> float:
        output = (
            float(self.significand * (self.radix ** self.exponent))
            if self.exponent >= 0 
            else self.significand / (self.radix ** -self.exponent))
        # NOTE: since IEEE 754 guarantees that division is always fully accurate, this will be faithful
        
        if Fraction.from_float(output) != Fraction(self):
            raise ValueError('this constant cannot be represented exactly as a float')

        return output

    def __pos__(self) -> Float:
        return Float(+self.significand, self.radix, self.exponent)
    
    def __neg__(self) -> Float:
        return Float(-self.significand, self.radix, self.exponent)
    
    def __abs__(self) -> Float:
        return Float(abs(self.significand), self.radix, self.exponent)
    
    def __floor__(self) -> Integral:
        ...

    def __ceil__(self) -> Integral:
        ...

    def __trunc__(self) -> Integral:
        ...

    def __round__(self, ndigits=None) -> Integral:
        ...

    def __lt__(self, other) -> bool:
        return Fraction(self) < Fraction(other)

    def __le__(self, other) -> bool:
        return Fraction(self) <= Fraction(other)

    def __eq__(self, other) -> bool:
        return Fraction(self) == Fraction(other)
    
    def __add__(self, other) -> Float:
        # 1.2 * 3 ** 4
        # 5.6 * 7 ** 8
        ...

    def __mul__(self, other) -> Float:
        ...

    def __truediv__(self, other) -> Float:
        ...

    def __pow__(self, other) -> Float:
        ...

    def __floordiv__(self, other) -> Float:
        ...

    def __mod__(self, other) -> Float:
        ...

    def __radd__(self, other) -> Float:
        return self + other

    def __rmul__(self, other) -> Float:
        return self * other

    def __rtruediv__(self, other) -> Float:
        return self / other

    def __rpow__(self, other) -> Float:
        return self ** other

    def __rfloordiv__(self, other) -> Float:
        return self // other
    
    def __rmod__(self, other) -> Float:
        return self % other
    
    def __str__(self) -> str:
        return f'({self.significand} * {self.radix} ** {self.exponent})'

