#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
from fabric.api import lcd
from fabric.operations import local

DIR_REPOS = os.path.join(
    os.path.dirname(__file__),
    '../../downloads')


def git_clone(repo, url):
    if not os.path.exists(DIR_REPOS):
        os.makedirs(DIR_REPOS)
    repo_dir = os.path.join(DIR_REPOS, repo)
    with lcd(DIR_REPOS):
        if (local('git clone {0}'.format(url)).succeeded and
                os.path.exists(repo_dir)):
            return repo_dir
        else:
            return None


def git_push(dir, target):
    with lcd(dir):
        local('for remote in `git branch -r`; '
              'do git branch --track $remote; done')
        return local('git push {0} --all'.format(target)).succeeded
