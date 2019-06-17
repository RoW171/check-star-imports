#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robin 'r0w' Weiland"
__credits__ = ["Robin Weiland", ]
__copyright__ = "Copyright 2019, Robin Weiland"

__date__ = "2019-06-17"
__version__ = "0.0.1"
__license__ = "MIT"

__all__ = ['check_star_imports']
__doc__ = """compares globals() before and after the import; used as a contextmanager
basic example:

>>> from checkstarimports import check_star_imports
>>> with check_starred_imports():
    from pyglet.gl import *


9214 objects were imported!

 for more examples see readme"""


class check_star_imports:  # I know underscores and lowercase in classes... but it looks better as contextmanager
    __doc__ = __doc__
    __slots__ = ['start_count']  # saves 8 bytes

    def __init__(self):
        self.start_count: int = 0

    def __enter__(self, *args, **kwargs):
        """runs before imports"""
        self.start_count = len(globals())  # not in __init__ for reusability

    def __exit__(self, *args, **kwargs):
        """ runs after imports"""
        number: int = len(globals()) - self.start_count
        print(f'{number} {"objects were" if number == 1 else "object was"} imported!')


if __name__ == '__main__': help(check_star_imports)
