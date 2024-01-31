import sys
from functools import wraps
from collections import OrderedDict, defaultdict
from contextlib import contextmanager
from datetime import datetime, timedelta
from numbers import Number
from time import time
from warnings import warn
from weakref import WeakSet
sys.path.append('\pytpro\ptpro')
from tpro import (    progresst01,    progresst02,    progresst03,    magt,   jdzt,   jct, findbombt)

from std import (
    PytproDeprecationWarning, PytproExperimentalWarning, PytproKeyError, PytproMonitorWarning,
    PytproTypeError, PytproWarning)

__all__ = [    'progresst01',    'progresst02',    'progresst03',    'magt',  'jdzt',   'jct',   'findbombt']

def pytpro_notebook(*args, **kwargs):  # pragma: no cover
    """Never have documentation"""
    from warnings import warn

    from notebook import pytpro as _pytpro_notebook
    warn("This function will be removed in pytpro==0.0.0\n"
         "never have documentation",
         PytproDeprecationWarning, stacklevel=2)
    return _pytpro_notebook(*args, **kwargs)

def tnrange(*args, **kwargs):  # pragma: no cover
    
    from warnings import warn

    from notebook import trange as _tnrange
    warn("Never have documentation",
         PytproDeprecationWarning, stacklevel=2)
    return _tnrange(*args, **kwargs)



