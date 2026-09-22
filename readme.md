# daamath-python
python implementation of [daamath](https://deftasparagusanaconda.github.io/daamath)

# install

get it from [PyPI](https://pypi.org/project/daamath):

```sh
python -m pip install daamath
```

or get it from [GitHub](https://github.com/deftasparagusanaconda/daamath-python):

```shell
git clone https://github.com/deftasparagusanaconda/daamath-python
pip install -e ./daamath-python
```

you may have to [set up a venv](https://docs.python.org/3/library/venv.html#creating-virtual-environments). once youre done, test daamath:

```python
import daamath as dm

print(dm.sqrt(4))
# 2
```

# quirks

here, we document the places where the implementation does not conform to the specification

`dm.unicode.greek.lower.lambda` is stored as `dm.unicode.greek.lower.lambda_` due to clash with python keyword `lambda`


