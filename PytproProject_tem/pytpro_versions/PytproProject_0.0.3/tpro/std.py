import sys
from collections import OrderedDict, defaultdict
from contextlib import contextmanager
from datetime import datetime, timedelta
from numbers import Number
from time import time
from warnings import warn
from weakref import WeakSet
sys.path.append('\tpro')
from tpro import (    progresst_01,    progresst_02,    progresst_03,    mag)

__author__ = ""
__all__ = ['progresst_01', 'progresst_02', 'progresst_03', 'mag']

class PytproTypeError(TypeError):
    pass


class PytproKeyError(KeyError):
    pass


class PytproWarning(Warning):
    
    def __init__(self, msg, fp_write=None, *a, **k):
        if fp_write is not None:
            fp_write("\n" + self.__class__.__name__ + ": " + str(msg).rstrip() + '\n')
        else:
            super(PytproWarning, self).__init__(msg, *a, **k)


class PytproExperimentalWarning(PytproWarning, FutureWarning):
    """beta feature, unstable API and behaviour"""
    pass


class PytproDeprecationWarning(PytproWarning, DeprecationWarning):
    # not suppressed if raised
    pass


class PytproMonitorWarning(PytproWarning, RuntimeWarning):
    
    pass

def TRLock(*args, **kwargs):
    """threading RLock"""
    try:
        from threading import RLock
        return RLock(*args, **kwargs)
    except (ImportError, OSError):  # pragma: no cover
        pass


class PytproDefaultWriteLock(object):
    
    th_lock = TRLock()

    def __init__(self):
        
        cls = type(self)
        root_lock = cls.th_lock
        if root_lock is not None:
            root_lock.acquire()
        cls.create_mp_lock()
        self.locks = [lk for lk in [cls.mp_lock, cls.th_lock] if lk is not None]
        if root_lock is not None:
            root_lock.release()

    def acquire(self, *a, **k):
        for lock in self.locks:
            lock.acquire(*a, **k)

    def release(self):
        for lock in self.locks[::-1]:  # Release in inverse order of acquisition
            lock.release()

    def __enter__(self):
        self.acquire()

    def __exit__(self, *exc):
        self.release()

    @classmethod
    def create_mp_lock(cls):
        if not hasattr(cls, 'mp_lock'):
            try:
                from multiprocessing import RLock
                cls.mp_lock = RLock()
            except (ImportError, OSError):  # pragma: no cover
                cls.mp_lock = None

    @classmethod
    def create_th_lock(cls):
        assert hasattr(cls, 'th_lock')
        warn("create_th_lock not needed anymore", PytproDeprecationWarning, stacklevel=2)


