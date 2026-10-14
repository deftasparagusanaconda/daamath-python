import math, struct

class binary64(float):
    'a subclass of float with additional features for daamath'

    def __init__(self, value):
        self.value = value
    
    @staticmethod
    def nan(payload: int) -> binary64:
        if not 1 <= payload < 2**52:
            raise ValueError("payload must be in [1, 2**52)")
        
        bits = (0x7ff << 52) | payload
        return struct.unpack(">d", struct.pack(">Q", bits))[0]
    
# constants
binary64.radix           = binary64(    2.0)
binary64.precision       = binary64(   53.0)
binary64.emin            = binary64(-1022.0)
binary64.emax            = binary64(+1023.0)

binary64.epsilon         = binary64(math.ldexp(               1, +  52))
binary64.normal_min      = binary64(math.ldexp(               1, -1022))
binary64.normal_max      = binary64(math.ldexp(9007199254740991, + 971))
binary64.subnormal_min   = binary64(math.ldexp(               1, -1074))
binary64.subnormal_max   = binary64(math.ldexp(4503599627370495, -1074))

binary64.archimedes      = binary64(math.pi)
binary64.euler_bernoulli = binary64(math.e)
binary64.hartl           = binary64(math.tau)
