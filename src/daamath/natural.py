import numbers as _numbers

class natural(_numbers.Integral):
    def __init__(self, value):
        if value % 1 != 0 or value < 0:
            raise ValueError(f'{value} should be an integer ≥ 0')
        self.value = value

