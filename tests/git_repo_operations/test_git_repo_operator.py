#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import shutil
import tempfile
from easy_fork.git_repo_operations.git_repo_operator import (
    git_clone_to_dir,
    # git_push
)


def test_git_clone_to_dir():
    repo = 'easy-fork'
    url = 'https://github.com/huntzhan/easy-fork.git'
    try:
        local_repos_dir = tempfile.mkdtemp()
        repo_dir = git_clone_to_dir(repo, url, local_repos_dir)
        assert repo_dir is not None
    finally:
        shutil.rmtree(local_repos_dir)


def test_git_push():
    pass
