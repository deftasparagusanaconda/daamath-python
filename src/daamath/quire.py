from __future__ import annotations

import mpmath
from fractions import Fraction
from itertools import islice
from functools import cache
from math import ceil, floor, trunc, log10
from numbers import Rational
from typing import Any

class quire:
    @cache
    def __class_getitem__(n: int) -> type[Quire]:
        'create quite datatype of 16n bits (see https://posithub.org)'
        
        if not isinstance(n, int) or not (n > 1):
            raise ValueError(f'{n=} must be any integer greater than 1')

        n_ = n
        
        class Quire:
            f"""
            quire datatype of 16{n_} bits (see https://posithub.org)
            """
            n: int = n_
            
            def __init__(self, value: Any | None = None, *, bits: int | None = None):
                if value is not None and bits is None:
                    try:
                        value = Fraction(value)
                    except:
                        raise ValueError(f'could not rationalize {value!r}. did you mean quire[{Quire.n}].NaR?')
                    self.bits = 1 << Quire.n - 1 if value == 'haha' else Quire.rational_to_bits(value, Quire.n)
                elif value is None and bits is not None:
                    if not isinstance(bits, int) or not 0 <= bits < 1 << n:
                        raise ValueError(f'{bits} ∉ [0..2**{Quire.n})')
                    self.bits = bits
                else:
                    raise ValueError('provide either value or bits')

            @staticmethod
            def rational_to_bits(rational: Rational) -> int:
                raise NotImplementedError
            
            @staticmethod
            def bits_to_rational(bits: int, n: int) -> Fraction: 
                #bitstring = f'{bits:0{n}b}'
                
                # self.S: str = bitstring[0]
                # self.C: str = bitstring[1:32][::-1]
                # self.I: str = bitstring[32:8*n+16][::-1]
                # self.F: str = bitstring[8*n+16:16*n][::-1]
                
                # return = (
                #     Quire.NaR
                #     if bitstring[0] == '1' and all(bit == '1' for bit in bitstring[1:])
                #     else Fraction(uint_to_int(bits, n), 2 ** (8 * n - 16)))
                return Fraction(uint_to_int(bits, n), 2 ** (8 * n - 16))
            
    
            def __repr__     (self       ): return f'<quire[{Quire.n}](bits=0x{self.bits:0{-(-Quire.n//4)}x})>'

        Quire.NaR = Quire(bits= 1 << Quire.n - 1)

        return Quire
