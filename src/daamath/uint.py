from __future__ import annotations

from functools import cache

class uint:
    @cache
    def __class_getitem__(n: int):

        n_ = n
        class Uint:
            n = n_
            def __init__(self, bits: int):
                if not isinstance(bits, int) or not 0 < bits < 2 ** self.n:
                    raise ValueError(f'{bits} is not an int in [0, 2 ** {self.n})')
                self.bits: int = bits
            
            def __add__    (self, other): return Uint(self.bits + other.bits)
            def __sub__    (self, other): return Uint(self.bits - other.bits)
            def __mul__    (self, other): return Uint(self.bits * other.bits)
            def __truediv__(self, other): return Uint(self.bits / other.bits)
            def __repr__   (self): return f'<uint[{self.n}](0x{self.bits:0{-(-Uint.n//4)}x})>'
            def __str__    (self): return str(self.bits)
        
        Uint.max = Uint(bits = 1 << n - 1)

        return Uint
