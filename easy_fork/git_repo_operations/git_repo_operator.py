#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import shutil
from fabric.api import lcd
from fabric.operations import local


def git_clone_to_dir(repo, url, local_repos_dir):
    if not os.path.exists(local_repos_dir):
        os.makedirs(local_repos_dir)
    repo_dir = os.path.join(local_repos_dir, repo)
    try:
        with lcd(local_repos_dir):
            if (local('git clone {0}'.format(url)).succeeded and
                    os.path.exists(repo_dir)):
                return repo_dir
    except:
        pass
    if os.path.exists(repo_dir):
        shutil.rmtree(repo_dir)
    return None


def git_track_all_branches(repo_dir):
    import StringIO
    with lcd(repo_dir):
        remotes = StringIO.StringIO(local('git branch -r', capture=True))
        for line in remotes:
            remote = line.strip().split(' ')[0]
            local('git branch --track {0}'.format(remote))


def git_push(dir, target):
    with lcd(dir):
        local('for remote in `git branch -r`; '
              'do git branch --track $remote; done')
        return local('git push {0} --all'.format(target)).succeeded
