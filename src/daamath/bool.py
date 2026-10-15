#from builtins import bool as bool
import builtins as _builtins

class bool:
    "why a separate class? because python's bool is an instance of int, which is mathematically unacceptable. furthermore, i cant subclass bool, because it is a final class. so here we fucken are"
    def __init__(self, value):
        self.value: _builtins.bool = _builtins.bool(value)

    @classmethod
    def not_(cls, a):
        return cls(not cls(a))
    
    @classmethod
    def and_(cls, a, b):
        return cls(cls(a) and cls(b))
    
    @classmethod
    def or_(cls, a, b):
        return cls(cls(a) or cls(b))

    @classmethod
    def xor(cls, a, b):
        return cls(cls(a) ^ cls(b))
    
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
    
    def __not__ (self): return bool(self.value)
    def __and__ (self, other): return bool(self.value and other.value)
    def __or__  (self, other): return bool(self.value or other.value)
    #def __xor__  (self, other): return bool(self.value ^ other.value) # dont include this. this shit is a bitwise operation, not a boolean operation

    # python expects builtins.bool return type here, but i already have __bool__ so it shouldnt cause problems
    def __eq__  (self, other): return bool(self.value == other.value)
    def __ne__  (self, other): return bool(self.value != other.value)

    def __bool__(self): return self.value
    def __repr__(self): return f'<bool({self.value})>'
    def __str__ (self): return 'true' if self else 'false'
    
bool.false = bool(False)
bool.true = bool(True)
