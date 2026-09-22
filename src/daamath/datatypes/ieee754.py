import math
from numbers import Rational, Integral
from fractions import Fraction
from dataclasses import dataclass
from operator import index

@dataclass(frozen=True, slots=True)
class bigfloat(Rational):
    "a rational number with a 'floating' radix point"

    significand: int
    radix: int
    exponent: int
    
    def __post_init__(self):
        # if sig is 0, canonical exp is 0
        if self.significand == 0:
            object.__setattr__(self, 'exponent', 0)
            return
        
        # canonicalize to reduced form
        significand = self.significand
        exponent = self.exponent
        while significand % self.radix == 0:
            significand //= self.radix
            exponent += 1
        
        object.__setattr__(self, 'significand', significand)
        object.__setattr__(self, 'exponent', exponent)
    def as_integer_ratio(self) -> tuple[int, int]:
        if self.exponent >= 0:
            return self.significand * self.radix ** self.exponent, 1

        numerator = self.significand
        denominator = self.radix ** -self.exponent
        common = math.gcd(abs(numerator), denominator)

        return numerator // common, denominator // common

    @property
    def numerator(self) -> int:
        return self.as_integer_ratio()[0]

    @property
    def denominator(self) -> int:
        return self.as_integer_ratio()[1]   
    
    @classmethod
    def from_str(cls, string: str, *, radix: int = 10, exponent_marker: str = 'e') -> bigfloat:
        'construct a bigfloat from a string. radix=10 by default (like builtins.int). allows radix up to 36 with 0-9, a-z (just like builtins.int). exponent_marker is case-sensitive.'
        # special edge case
        if string in {'', '+', '-'}:
            raise ValueError(f'invalid bigfloat literal {string!r}')

        if exponent_marker.lower() in '0123456789abcdefghijklmnopqrstuvwxyz'[:radix]:
            raise ValueError(f'{exponent_marker=} is a character in {radix=}')
        # '-01.23e-45'
        sig_str, exp_str = string.split(exponent_marker, 1) if exponent_marker in string else (string, '0')
        # '-01.23', '-45'
        negative = sig_str.startswith('-')
        sig_str = sig_str.lstrip('+-')
        # -ve, '01.23', '-45'
        pre_str, post_str = sig_str.split('.', 1) if '.' in sig_str else (sig_str, '')
        # -ve, '01', '23', '-45'
        pre_str = pre_str.lstrip('0')
        post_str = post_str.rstrip('0')
        # -ve, '1', '23', '-45'

        # this is not the most efficient way. but it is understandable
        
        sig = int('-'*negative + pre_str + post_str, base=radix)
        exp = int(exp_str, base=radix) - len(post_str)
        
        return cls(sig, radix, exp)
    
    # ai-generated
    def _round_shift(self, shift: int) -> bigfloat:
        ''
        if shift <= 0:
            return self
        
        divisor = self.radix ** shift
        sign = -1 if self.significand < 0 else +1
        q, r = divmod(abs(self.significand), divisor)
    
        q += (2 * r > divisor) or (2 * r == divisor and q % 2)
        
        return type(self)(sign * q, self.radix, self.exponent + shift)

    def _digit_count(self) -> int:
        count = 0
        sig = self.significand
        while sig:
            count += 1
            sig //= self.radix
        return count
        
    def round_ndigits(self, ndigits: int = 0) -> bigfloat:
        return self._round_shift(-index(ndigits) - self.exponent)
    
    def round_sigfigs(self, sigfigs: int) -> bigfloat:
        sigfigs = index(sigfigs)
        if sigfigs <= 0:
            raise ValueError(f'{sigfigs=} must be positive')
        return self._round_shift(self._digit_count() - sigfigs)

    __round__ = round_ndigits
    
    # @classmethod
    # def from_rational(cls, rational: Rational, radix: int) -> bigfloat:
    #     numerator = abs(rational.numerator)
    #     denominator = rational.denominator
    #
    #     exponent = 0
    #     while numerator % radix == 0:
    #         numerator //= radix
    #         exponent += 1
    #     while denominator % radix == 0:
    #         denominator //= radix
    #         exponent -= 1
    #
    #     if denominator != 1:
    #         raise ValueError(f'{rational!r} is not finite in {radix=}')
    #
    #     return cls(-significand if rational < 0 else significand, radix, exponent)
    
    @classmethod
    def _from_integer_ratio_exact(cls, numerator: Integral, denominator: Integral, radix: int):
        if radix < 2:
            raise ValueError('radix must be >= 2')

        significand = abs(numerator)
        exponent = 0
        
        while significand and significand % radix == 0:
            significand //= radix
            exponent += 1
        
        while denominator != 1:
            if (common := math.gcd(denominator, radix)) == 1:
                raise ValueError(f'{numerator}/{denominator} is not finite in radix {radix}')
        
            denominator //= common
            significand *= radix // common
            exponent -= 1
        
        return cls(-significand if numerator < 0 else significand, radix, exponent)

    # ai-generated. i just need it working for now
    @classmethod
    def _from_integer_ratio_rounded(cls, numerator: Integral, denominator: Integral, radix: int, precision: int):
        assert denominator > 0, f'got {numerator=}, {denominator=}, {radix=}, {precision=}'
        assert math.gcd(abs(numerator), denominator) == 1, f'got {numerator=}, {denominator=}, {radix=}, {precision=}'
        if radix < 2:
            raise ValueError('radix must be >= 2')
        if precision <= 0:
            raise ValueError(f'{precision=} must be positive')
        if numerator == 0:
            return cls(0, radix, 0)

        magnitude = abs(numerator)

        if magnitude >= denominator:
            magnitude_exponent = 0
            boundary = denominator
            while magnitude >= boundary * radix:
                boundary *= radix
                magnitude_exponent += 1
        else:
            magnitude_exponent = -1
            scaled = magnitude * radix
            while scaled < denominator:
                scaled *= radix
                magnitude_exponent -= 1

        exponent = magnitude_exponent - precision + 1

        if exponent < 0:
            scaled_numerator = magnitude * radix ** -exponent
            scaled_denominator = denominator
        else:
            scaled_numerator = magnitude
            scaled_denominator = denominator * radix ** exponent

        significand, remainder = divmod(scaled_numerator, scaled_denominator)

        significand += (2 * remainder > scaled_denominator) or (2 * remainder == scaled_denominator and significand % 2)
        
        return cls(-significand if numerator < 0 else significand, radix, exponent)

    @classmethod
    def from_rational(cls, rational: Rational, radix: int, precision: int | None = None):
        if precision is None:
            return cls._from_integer_ratio_exact(rational.numerator, rational.denominator, radix)
        else:
            return cls._from_integer_ratio_rounded(rational.numerator, rational.denominator, radix, precision)
    
    def __pos__(self): return self
    def __neg__(self): return type(self)(-self.significand, self.radix, self.exponent)
    def __abs__(self): return type(self)(abs(self.significand), self.radix, self.exponent)
    def __ceil__(self): return bigfloat.from_rational(math.ceil(Fraction(self)))
    def __floor__(self): return bigfloat.from_rational(math.floor(Fraction(self)))
    def __trunc__(self): return bigfloat.from_rational(math.trunc(Fraction(self)))
    def __floordiv__(self, other): return bigfloat.from_rational(Fraction(self) // Fraction(other))
    def __mod__(self, other): return bigfloat.from_rational(Fraction(self) % Fraction(other))
    def __le__(self, other): return Fraction(self) <= Fraction(other)
    def __lt__(self, other): return Fraction(self) < Fraction(other)
    def __add__(self, other): return Fraction(self) + Fraction(other)
    def __mul__(self, other): return bigfloat.from_rational(Fraction(self) * Fraction(other))
    def __truediv__(self, other): return bigfloat.from_rational(Fraction(self) / Fraction(other))
    def __pow__(self, other): return bigfloat.from_rational(Fraction(self) ** Fraction(other))
    def __rfloordiv__(other, self): return bigfloat.from_rational(Fraction(self) // Fraction(other))
    def __radd__(other, self): return bigfloat.from_rational(Fraction(self) + Fraction(other))
    def __rmul__(other, self): return bigfloat.from_rational(Fraction(self) * Fraction(other))
    def __rmod__(other, self): return bigfloat.from_rational(Fraction(self) % Fraction(other))
    def __rpow__(other, self): return bigfloat.from_rational(Fraction(self) ** Fraction(other))
    def __rtruediv__(other, self): return bigfloat.from_rational(Fraction(self) / Fraction(other))
    
    def __float__(self) -> float:
        return float(Fraction(self))
    def __int__(self) -> int:
        return int(Fraction(self))

    def __str__(self) -> str:
        return f'({self.significand} * {self.radix} ** {self.exponent})'
    
'''
def ieee_binary(bits: int) -> type:
    match bits: 
        case 16: precision = 11; emin = -  14; emax =   15
        case 32: precision = 24; emin = - 126; emax =  127
        case 64: precision = 53; emin = -1022; emax = 1023
        case  _:
            if bits < 128 or bits % 32 != 0:
                raise ValueError('IEEE defines interchange formats for bits: 16, 32, 64, and multiples of 32 ≥128')
        
            exponent_digits = round(4 * math.log2(bits)) - 13
            precision = bits - exponent_digits
            emax = 2 ** (exponent_digits - 1) - 1
            emin = 1 - emax

    class IEEE754Binary(bigfloat):
        'an IEEE 754 binary float'
    
        def __init__(self, significand: int, exponent: int):
            super().__init__(radix=2, precision=precision, significand=significand, exponent=exponent)

        @classmethod
        def from_str(cls, string) -> IEEE754Binary:
            return super().from_str(string, radix = 2, precision = precision)
    
    return IEEE754Binary

def ieee_decimal(bits: int) -> type:
    match bits:
        case 32: precision =  7; emin = - 95; emax =  96
        case 64: precision = 16; emin = -383; emax = 384
        case  _:
            if bits < 128 or bits % 32 != 0:
                raise ValueError('IEEE defines interchange formats for bits: 32, 64, and multiples of 32 ≥128')
            
            precision = 9 * (bits // 32) - 2
            emax = 3 * 2 ** ((2 * (bits // 32) + 4) - 1)
            emin = 1 - emax

    class IEEE754Decimal(bigfloat):
        'an IEEE 754 decimal float'
    
        def __init__(self, significand: int, exponent: int):
            super().__init__(radix=10, precision=precision, significand=significand, exponent=exponent)
        
        @classmethod
        def from_str(cls, string, *, radix = 10) -> IEEE754Decimal:
            return super().from_str(string, radix = radix, precision = precision)
        
    return IEEE754Decimal

#f16  = ieee_binary( 16)
f32  = ieee_binary( 32)
f64  = ieee_binary( 64)
f128 = ieee_binary(128)
#f256 = ieee_binary(256)

#d32  = ieee_decimal( 32)
d64  = ieee_decimal( 64)
d128 = ieee_decimal(128)
'''

'''
f16:
0 00000 0000000000
False/True 00001–11110 0000000000
−/+ [−14, +15] [0/2E10, 1023/2E10]

d32:
0 000 0000000
−/+ −95, +96] [0/1E7, 9999999/1E7]
'''

class binary64(float):
    'a subclass of float with additional functions for daamath'

binary32 = None
binary128 = None
decimal64 = None
decimal128 = None
