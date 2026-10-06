from ..implementation_specific_things import Constant as _Constant
import math as _math

class binary32:
    epsilon       = _Constant(                                  1,  2, -   23)
    normal_min    = _Constant(                                  1,  2, -  126)
    normal_max    = _Constant(                           16777215,  2, +  104)
    subnormal_min = _Constant(                                  1,  2, -  149)
    subnormal_max = _Constant(                            8388607,  2, -  149)
class binary64:
    #nan = _math.nan
    pos_inf = float('+inf')
    neg_inf = float('-inf')
    pos_zero = +0.0
    neg_zero = -0.0
    epsilon       = _Constant(                                  1,  2, -   52)
    normal_min    = _Constant(                                  1,  2, - 1022)
    normal_max    = _Constant(                   9007199254740991,  2, +  971)
    subnormal_min = _Constant(                                  1,  2, - 1074)
    subnormal_max = _Constant(                   4503599627370495,  2, - 1074)
class binary128:
    epsilon       = _Constant(                                  1,  2, -  112)
    normal_min    = _Constant(                                  1,  2, -16382)
    normal_max    = _Constant(10384593717069655257060992658440191,  2, +16271)
    subnormal_min = _Constant(                                  1,  2, -16494)
    subnormal_max = _Constant( 5192296858534827628530496329220095,  2, -16494)
class decimal64:
    epsilon       = _Constant(                                  1, 10, -   15)
    normal_min    = _Constant(                                  1, 10, -  383)
    normal_max    = _Constant(                   9999999999999999, 10, +  369)
    subnormal_min = _Constant(                                  1, 10, -  398)
    subnormal_max = _Constant(                    999999999999999, 10, -  398)
class decimal128:
    epsilon       = _Constant(                                  1, 10, -   33)
    normal_min    = _Constant(                                  1, 10, - 6143)
    normal_max    = _Constant( 9999999999999999999999999999999999, 10, + 6111)
    subnormal_min = _Constant(                                  1, 10, - 6176)
    subnormal_max = _Constant(  999999999999999999999999999999999, 10, - 6176)

class int8:
    min = _Constant(-1,  2, +    7)
    max = _Constant(+1,  2, +    7) - 1
class int16:
    min = _Constant(-1,  2, +   15)
    max = _Constant(+1,  2, +   15) - 1
class int32:
    min = _Constant(-1,  2, +   31)
    max = _Constant(+1,  2, +   31) - 1
class int64:
    min = _Constant(-1,  2, +   63)
    max = _Constant(+1,  2, +   63) - 1
class int128:
    min = _Constant(-1,  2, +  127)
    max = _Constant(+1,  2, +  127) - 1

class uint8:
    min = _Constant( 0,  2,      0)
    max = _Constant( 1,  2,      8) - 1
class uint16:
    min = _Constant( 0,  2,      0)
    max = _Constant( 1,  2,     16) - 1
class uint32:
    min = _Constant( 0,  2,      0)
    max = _Constant( 1,  2,     32) - 1
class uint64:
    min = _Constant( 0,  2,      0)
    max = _Constant( 1,  2,     64) - 1
class uint128:
    min = _Constant( 0,  2,      0)
    max = _Constant( 1,  2,    128) - 1
