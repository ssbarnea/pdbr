# pdbr

[![PyPI version](https://badge.fury.io/py/pdbr.svg)](https://pypi.org/project/pdbr/) [![Python Version](https://img.shields.io/pypi/pyversions/pdbr.svg)](https://pypi.org/project/pdbr/) [![](https://github.com/cansarigol/pdbr/workflows/Release/badge.svg)](https://github.com/cansarigol/pdbr/actions?query=workflow%3ARelease) [![](https://github.com/cansarigol/pdbr/workflows/Test/badge.svg)](https://github.com/cansarigol/pdbr/actions?query=workflow%3ATest)

[Rich](https://github.com/willmcgugan/rich) is a great library for terminal output. In order to make the PDB results more colorful.

## Installing

Install with `pip` or your favorite PyPi package manager.

```
pip install pdbr
```

## Breakpoint

In order to use ```breakpoint()```, set **PYTHONBREAKPOINT** with "pdbr.set_trace"

```python
import os

os.environ["PYTHONBREAKPOINT"] = "pdbr.set_trace"
```

or just import pdbr

```python
import pdbr
```

## Config
In order to use Rich's traceback, style, and theme, set **setup.cfg**.

```
[pdbr]
style = yellow
use_traceback = True
theme = friendly
```

## Samples
### The difference from PDB
![](/samples/sample1.png)

### Traceback
![](/samples/sample2.png)
