# test

from __future__ import annotations

import mpmath
from fractions import Fraction
from itertools import islice
from functools import cache
from math import ceil, floor, trunc, log10
from numbers import Rational
from typing import Any
from .int import int_to_uint, uint_to_int

class posit:
    'yo sup lmao'
    @cache
    def __class_getitem__(n: int) -> type[Posit]:
        'create posit datatype of n bits (see https://posithub.org)'
        
        if not isinstance(n, int) or not (n > 1):
            raise ValueError(f'{n=} must be any integer greater than 1')
        
        n_ = n
        class Posit:
            f"""
            posit datatype of {n_} bits (see https://posithub.org)
            """
            n = n_
            
            def __init__(self, value: Any | None = None, *, bits: int | None = None):
                if value is not None and bits is None:
                    try:
                        value = Fraction(value)
                    except:
                        raise ValueError(f'could not encode {value}. did you mean posit[{Posit.n}].NaR?')
                    self.bits = 1 << Posit.n - 1 if value == 'haha' else Posit.rational_to_bits(value, Posit.n)
                elif value is None and bits is not None:
                    if not isinstance(bits, int) or not 0 <= bits < 1 << n:
                        raise ValueError(f'{bits} ∉ [0..2**{Posit.n})')
                    self.bits = bits
                else:
                    raise ValueError('provide either value or bits')

            def as_integer_ratio(self) -> tuple[int, int]:
                if self.bits == Posit.NaR.bits:
                    raise ValueError(f'Not a Real')
                return Posit.bits_to_rational(self.bits, Posit.n).as_integer_ratio()
            @property
            def numerator(self) -> int:
                return self.as_integer_ratio()[0]
            @property
            def denominator(self) -> int:
                return self.as_integer_ratio()[1]
            
            @staticmethod
            def bits_to_rational(bits: int, n: int) -> Fraction:
                # the shit variable names are from the spec directly. dont blame me okay
                
                if bits == 0:
                    return Fraction(0)
                
                # split into S R E F
                
                it = iter(f'{bits:0{n}b}')
                
                S: str = next(it)      
                R: str = next(it)
                for bit in it:
                    if bit != R[-1]:
                        break
                    R += bit
                E: str = ''.join(islice(it, 2))
                F: str = ''.join(it)
                R_0: str = R[-1]
                
                # calculate p
                
                k: int = len(R)
                m: int = len(F)
                
                s: int = int(S)
                r: int = k - 1 if int(R_0) else -k
                e: int = int(E.ljust(2, '0'), base=2)
                f: Fraction = Fraction(int(F or '0', base=2), 2 ** m)
                
                return ((1 - 3 * s) + f) * 2 ** ((1 - 2 * s) * (4 * r + e + s))
                
            @staticmethod
            def rational_to_bits(x: Rational, n: int) -> int:
                lo = 1 - (1 << (n - 1))
                hi =     (1 << (n - 1)) - 1
                
                while lo + 1 < hi:
                    mid = (lo + hi) // 2
                    mid_value = Posit.bits_to_rational(int_to_uint(mid, n), n)
                    
                    if x > mid_value:
                        lo = mid
                    elif x < mid_value:
                        hi = mid
                    else:
                        return int_to_uint(mid, n)
                
                v = Posit.bits_to_rational((int_to_uint(lo, n) << 1) + 1, n + 1)
                return int_to_uint(lo if x < v or (x == v and int_to_uint(lo, n) & 1 == 0) else hi, n)
            
            # def as_dyadic_rational(self) -> tuple[int, int]:
            #     numerator, denominator = self.as_integer_ratio()
            #     K = numerator
            #     M = 1 - denominator.bit_length()
            #
            #     while K != 0 and K % 2 == 0:
            #         K //= 2
            #         M += 1
            #
            #     return K, M
                
            # def as_hexponential(self) -> tuple[Fraction, int]:
            #     numerator, denominator = self.as_integer_ratio()
            # def __str__(self) -> str:
            #     if self == Posit.NaN:
            #         return 'NaR'
            #     fuwa, hoge = self.as_hexponential()
            #     return f"0x{fuwa}p{hoge:+}"
            
            @classmethod
            def sqrt(cls, x: Posit) -> Posit:
                mpmath.mp.dps = x.n * log10(2)
                return cls(mpmath.sqrt(x))
            
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
            def __pos__      (self       ): return Posit(   +Fraction(self)                     )
            def __neg__      (self       ): return Posit(   -Fraction(self)                     )
            def __abs__      (self       ): return Posit(abs(Fraction(self))                    )
            def __float__    (self       ): return float(    Fraction(self  )                   )
            def __int__      (self       ): return int  (    Fraction(self  )                   )
            def __bool__     (self       ): return bool (    Fraction(self  )                   )
            def __floor__    (self       ): return floor(    Fraction(self)                     )
            def __ceil__     (self       ): return ceil (    Fraction(self)                     )
            def __trunc__    (self       ): return trunc(    Fraction(self)                     )
            def __round__    (self, ndigits=None): return round(Fraction(self), ndigits=ndigits)
            def __hash__     (self       ): return hash(Fraction(self.bits))
            def __str__      (self       ): return 'NaR' if self.bits == self.NaR.bits else '0' if self == 0 else f'{float(self):+}'  # change this later to hexadecimal scientific notation
            def __repr__     (self       ): return f'<posit[{Posit.n}](bits=0x{self.bits:0{-(-Posit.n//4)}x})>'
        
        # why as instances, and not as simpler types?
        # because they also give you access to the bits representation for free
        Posit.NaR     = Posit(bits= 1 << Posit.n - 1)
        Posit.maxPos  = Posit(bits=(1 << Posit.n - 1) - 1) # 2 ** (+4 * n - 8)
        Posit.minPos  = Posit(bits= 1)                     # 2 ** (-4 * n + 8)
        Posit.pIntMax = Posit(ceil(2 ** (4 * (n - 3) // 5)))
        
        return Posit

    
