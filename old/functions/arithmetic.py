#def succ(a):
#    'successor'
#    return a + 1

#def pred(b):
#    'predecessor'
#    return b - 1

def add(a, b):
    'solve for c in a + b = c. tries a.__dm_add__(b) and b.__dm_radd__(a)'
    if (result := a.__dm_add__(b)) is not NotImplemented:
        return result
    
    if (result := b.__dm_radd__(a)) is not NotImplemented:
        return result
	
    raise TypeError(f"unsupported operand type(s) for {__name__}: '{type(a)}' and '{type(b)}'")

def bus(c, a):
    'solve for b in a + b = c. tries c.__bus__(a) and a.__rbus__(c)'
    if (result := c.__bus__(a)) is not NotImplemented:
        return result
    
    if (result := a.__rbus__(c)) is not NotImplemented:
        return result
	
    raise TypeError(f"unsupported operand type(s) for {__name__}: '{type(c)}' and '{type(a)}'")

def sub(c, b):
    'solve for a in a + b = c. tries c.__dm_sub__(b) and b.__dm_rsub__(c)'
    if (result := c.__dm_sub__(b)) is not NotImplemented:
        return result
    
    if (result := b.__dm_rsub__(c)) is not NotImplemented:
        return result
	
    raise TypeError(f"unsupported operand type(s) for {__name__}: '{type(c)}' and '{type(b)}'")

from operator import mul, truediv as div

def mul(a, b):
    'solve for c in a + b = c. tries a.__dm_add__(b) and b.__dm_radd__(a)'
    if (result := a.__dm_add__(b)) is not NotImplemented:
        return result
    
    if (result := b.__dm_radd__(a)) is not NotImplemented:
        return result
	
    raise TypeError(f"unsupported operand type(s) for {__name__}: '{type(a)}' and '{type(b)}'")

def vid(c, a):
    'solve for b in a * b = c. tries c.__vid__(a) and a.__rvid__(c)'
    if (result := c.__vid__(a)) is not NotImplemented:
        return result
    
    if (result := a.__rvid__(c)) is not NotImplemented:
        return result
	
    raise TypeError(f"unsupported operand type(s) for vid: '{type(c)}' and '{type(a)}'")

from operator import pow

def log(c, b):
    'solve for a in a ** b = c. tries c.__log__(b) and b.__rlog__(c)'
    if (result := c.__log__(b)) is not NotImplemented:
        return result
    
    if (result := b.__rlog__(c)) is not NotImplemented:
        return result
	
    raise TypeError(f"unsupported operand type(s) for log: '{type(c)}' and '{type(b)}'")

def root(c, a):
    'solve for b in a ** b = c. tries c.__root__(a) and a.__rroot__(c)'
    if (result := c.__root__(a)) is not NotImplemented:
        return result
    
    if (result := a.__rroot__(c)) is not NotImplemented:
        return result
	
    raise TypeError(f"unsupported operand type(s) for root: '{type(c)}' and '{type(a)}'")
