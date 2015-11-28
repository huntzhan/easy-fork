#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
from easy_fork.file_operators.gitlab_config import load_gitlab_config


def test_load_gitlab_config():
    gitlab_config_path = os.path.join(
        os.path.dirname(__file__),
        'gitlab_config_for_testing.py',
    )
    obj = load_gitlab_config(gitlab_config_path)
    assert 'http://xxx' == obj.api_prefix
    assert 'testuser' == obj.username
    assert 'testpassword' == obj.password
    assert '12345' == obj.token
    assert 'testgroup' == obj.groupname
