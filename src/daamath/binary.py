from __future__ import annotations

from functools import cache
from typing import Any
from fractions import Fraction
from numbers import Rational

class binary:
    @cache
    def __class_getitem__(n: int) -> Binary: 
        'construct an n bits IEEE754 Binary datatype'
        if not isinstance(n, int):
            raise TypeError(f'{n} must be an int')

        if not(n in (16, 32, 64, 128) or (n >= 128 and n % 32 == 0)):
            raise ValueError(f'{n} ∉ [16, 32, 64, 128] and (n < 128 or n % 32 != 0)')
        
        # i think this class needs to store its bitfield configuration because it *is* a constant, and i need it often
        n_ = n
        class Binary:
            f'IEEE754 Binary datatype of {n_} bits'

            n = n_
            
            def __init__(self, value: Any | None = None, *, bits: int | None = None):
                if value is not None and bits is None:
                    try:
                        value = Fraction(value)
                    except:
                        raise ValueError(f'could not encode {value}. did you mean binary[{Binary.n}].nan?')
                    self.bits = 1 << Posit.n - 1 if value == 'haha' else Posit.rational_to_bits(value, Posit.n)
                elif value is None and bits is not None:
                    if not isinstance(bits, int) or not 0 <= bits < 1 << n:
                        raise ValueError(f'{bits} ∉ [0..2**{Binary.n})')
                    self.bits = bits
                else:    
                    raise ValueError('provide either value or bits')
            
            @staticmethod
            def bits_to_rational(bits: int, n: int) -> Fraction:
                return ...

            @staticmethod
            def rational_to_bits(rational: Rational, n: int) -> int:
                return ...
            
            @classmethod
            def qnan(cls, payload: int) -> Binary:
                'construct a positive quiet NaN with given payload'
                if not isinstance(payload, int) or not 0 < payload < 2 ** n - 1:
                    raise ValueError('')
                return cls(bits=payload)

            @classmethod
            def qnan(cls, payload: int) -> Binary:
                'construct a positive quiet NaN with given payload'
                if not isinstance(payload, int) or not 0 < payload < 2 ** n - 1:
                    raise ValueError('')
                return cls(bits=payload)
        
            
            def __eq__       (self, other): return           Fraction(self  ) == Fraction(other)
            def __le__       (self, other): return           Fraction(self  ) <= Fraction(other)
            def __lt__       (self, other): return           Fraction(self  ) <  Fraction(other)
            def __floordiv__ (self, other): return           Fraction(self  ) // Fraction(other)
            def __mod__      (self, other): return           Fraction(self  ) %  Fraction(other)
            def __rfloordiv__(self, other): return           Fraction(other ) // Fraction(self )
            def __rmod__     (self, other): return           Fraction(other ) %  Fraction(self )
            def __add__      (self, other): return Posit(    Fraction(self  ) +  Fraction(other))
            def __sub__      (self, other): return Posit(    Fraction(self  ) -  Fraction(other))
            def __mul__      (self, other): return Posit(    Fraction(self  ) *  Fraction(other))
            def __truediv__  (self, other): return Posit(    Fraction(self  ) /  Fraction(other))
            def __pow__      (self, other): return Posit(    Fraction(self  ) ** Fraction(other))
            def __radd__     (self, other): return Posit(    Fraction(other ) +  Fraction(self ))
            def __rsub__     (self, other): return Posit(    Fraction(other ) -  Fraction(self ))
            def __rmul__     (self, other): return Posit(    Fraction(other ) *  Fraction(self ))
            def __rtruediv__ (self, other): return Posit(    Fraction(other ) /  Fraction(self ))
            def __rpow__     (self, other): return Posit(    Fraction(other ) ** Fraction(self ))
            def __pos__      (self       ): return Posit(   +Fraction(self  )                   )
            def __neg__      (self       ): return Posit(   -Fraction(self  )                   )
            def __abs__      (self       ): return Posit(abs(Fraction(self  ))                  )
            def __float__    (self       ): return float(    Fraction(self  )                   )
            def __int__      (self       ): return int  (    Fraction(self  )                   )
            def __bool__     (self       ): return bool (    Fraction(self  )                   )
            def __floor__    (self       ): return floor(    Fraction(self  )                   )
            def __ceil__     (self       ): return ceil (    Fraction(self  )                   )
            def __trunc__    (self       ): return trunc(    Fraction(self  )                   )
            def __round__    (self, ndigits=None): return round(Fraction(self), ndigits=ndigits)
            def __hash__     (self       ): return hash(Fraction(self.bits))
            def __str__      (self       ): return 'NaR' if self.bits == self.NaR.bits else '0' if self == 0 else f'{float(self):+}'  # change this later to hexadecimal scientific notation
            def __repr__     (self       ): return f'<posit[{Posit.n}](bits=0x{self.bits:0{-(-Posit.n//4)}x})>'
            
        inf = Binary(bits='')

        return Binary
