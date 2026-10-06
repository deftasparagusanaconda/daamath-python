from __future__ import annotations
from numbers import Integral

class uint8:
    def __init__(self, value: Integral):
        if value != int(value) or value < 0:
            raise ValueError(f'cannot convert {value} to uint8 faithfully')
        self.value: int = int(value)
    
    
# constants
uint8.max = uint8(255)
