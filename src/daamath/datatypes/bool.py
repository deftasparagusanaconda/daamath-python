#from builtins import bool as bool
import builtins as _builtins

class bool:
    def __init__(self, value):
        self.value = _builtins.bool(value)

    @classmethod
    def not_(cls, a):
        return cls(not a)
    
    @classmethod
    def and_(cls, a, b):
        return cls(a and b)
    
    @classmethod
    def or_(cls, a, b):
        return cls(a or b)

    @classmethod
    def xor(cls, a, b):
        return cls(a ^ b)
    
    @classmethod
    def imp(cls, a, b):
        return cls(not a or b)
    
    @classmethod
    def con(cls, a, b):
        return cls(a or not b)

    @classmethod
    def nand(cls, a, b):
        return cls(not(a and b))
    
    @classmethod
    def nor(cls, a, b):
        return cls(not(a or b))

    @classmethod
    def nxor(cls, a, b):
        return cls(not(a ^ b))
    
    @classmethod
    def nimp(cls, a, b):
        return cls(a and not b)
    
    @classmethod
    def ncon(cls, a, b):
        return cls(not a and b)
    
    def __bool__(self) -> _builtins.bool:
        return self.value
