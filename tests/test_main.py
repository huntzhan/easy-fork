# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

# remove following code.
from easy_fork.main import entry_point


def test_entry_point():
    assert 42 == entry_point()
