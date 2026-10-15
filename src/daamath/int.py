from functools import cache
from typing import Any
import builtins

def int_to_uint(x: builtins.int, n: builtins.int) -> builtins.int:
    if not -1 << n - 1 <= x < +1 << n - 1:
        raise ValueError(f'{x} ∉ [-2**{n-1}..+2**{n-1})')
    return x if x >= 0 else x + (1 << n)

def uint_to_int(x: builtins.int, n: builtins.int) -> builtins.int:
    if not 0 <= x < 1 << n:
        raise ValueError(f'{x} ∉ [0..2**{n})')
    return x if x < (1 << n - 1) else x - (1 << n)

class int:
    @cache
    def __class_getitem__(n: builtins.int):
        if not isinstance(n, builtins.int) or n < 1:
            raise ValueError('n must be an int greater than 0')
        
        n_ = n
        class Int:
            'a signed integer in [2**(n-1) .. 2**(n-1))'
            n = n_
            def __init__(self, value: Any | None = None, bits: int | None = None):
                if value is not None and bits is None:
                    self.bits = int_to_uint(builtins.int(value), Int.n)
                elif value is None and bits is not None:
                    if not isinstance(bits, builtins.int) or not 0 <= bits < 1 << n:
                        raise ValueError(f'{bits} ∉ [0 .. 2**{Int.n})')
                    self.bits = bits
                else:
                    raise ValueError('provide either value or bits')


            def __repr__(self): return f'<int[{Int.n}](bits=0x{self.bits:0{-(-Int.n//4)}x})>'
            def __str__ (self): return str(uint_to_int(self.bits, Int.n))
        
        Int.minPos = -2 ** (n - 1)
        Int.maxPos = +2 ** (n - 1) - 1

        return Int
