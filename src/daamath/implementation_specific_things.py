class Float:
    def __init__(self, significand: int, radix: int, exponent: int):
        self.significand: int = significand
        self.radix: int = radix 
        self.exponent: int = exponent

    def __int__(self) -> int:
        if unfaithful:
            raise ValueError('this constant cannot be represented as an int')
        raise NotImplementedError
        
    def __float__(self) -> float:
        if unfaithful:
            raise ValueError('this constant cannot be represented as a float')
        raise NotImplementedError

    def __str__(self) -> str:
        return f'{self.significand} * {self.radix} ** {self.exponent})'
    
    def __sub__(self, other) -> Float:
        ...
