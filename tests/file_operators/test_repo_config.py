#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
from easy_fork.file_operators.repo_config import (
    REPO_ID_TYPE_GITHUB,
    load_repo_config,
)


def test_github_repo_id():
    repo_config_path = os.path.join(
        os.path.dirname(__file__),
        'repo_config_for_testing.py',
    )
    repo_ids = load_repo_config(repo_config_path)
    assert 2 == len(repo_ids)
    test_id = repo_ids[0]
    assert REPO_ID_TYPE_GITHUB == test_id.repo_id_type
    assert 'huntzhan' == test_id.owner
    assert 'easy-fork' == test_id.repo
    assert 'huntzhan/easy-fork' == test_id.fullname
    assert 'https://github.com/huntzhan/easy-fork.git' == test_id.url
