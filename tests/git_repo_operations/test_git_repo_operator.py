#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import shutil
from easy_fork.git_repo_operations.git_repo_operator import (
    git_clone,
    # git_push
)


def test_git_clone():
    repo = 'easy-fork'
    url = 'https://github.com/huntzhan/easy-fork.git'
    repo_dir = git_clone(repo, url)
    assert repo_dir is not None
    shutil.rmtree(repo_dir)


def test_git_push():
    pass
