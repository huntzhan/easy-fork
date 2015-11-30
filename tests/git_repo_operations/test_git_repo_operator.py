#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import shutil
import tempfile
from fabric.api import lcd
from fabric.operations import local
from easy_fork.git_repo_operations.git_repo_operator import (
    git_clone_to_dir,
    git_track_all_branches,
    # git_push
)

repo = 'easy-fork'
url = 'https://github.com/huntzhan/easy-fork.git'


def test_git_clone_to_dir():
    local_repos_dir = tempfile.mkdtemp()
    try:
        repo_dir = git_clone_to_dir(repo, url, local_repos_dir)
        assert repo_dir is not None
    finally:
        shutil.rmtree(local_repos_dir)


def test_git_track_all_branches():
    local_repos_dir = tempfile.mkdtemp()
    try:
        repo_dir = git_clone_to_dir(repo, url, local_repos_dir)
        git_track_all_branches(repo_dir)
        with lcd(repo_dir):
            track_branches = local('git branch --track', capture=True)
            assert track_branches.find('master') >= 0
            # assert track_branches.find('origin/HEAD') >= 0
            # assert track_branches.find('origin/master') >= 0
    finally:
        shutil.rmtree(local_repos_dir)


def test_git_push():
    pass
