# daamath-python
python implementation of daamath

# install

daamath is hosted on [PyPI](https://pypi.org/project/daamath). simply run this in your terminal:

```sh
python -m pip install daamath
```

you may have to [set up a venv](https://docs.python.org/3/library/venv.html#creating-virtual-environments). once youre done, test daamath:

```python
import daamath as dm

print(dm.sqrt(4))
# 2
```

# quirks

here, we document the places where the implementation does not conform to the specification

the datatypes for f32, f128, d64, d128 are not available
`dm.unicode.greek.lower.lambda` is stored as `dm.unicode.greek.lower.lambda_` due to clash with python keyword `lambda`


