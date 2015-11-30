#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import shutil
import StringIO

from fabric.api import lcd
from fabric.operations import local
from fabric.context_managers import settings


def git_clone_to_dir(repo, url, local_repos_dir):
    if not os.path.exists(local_repos_dir):
        os.makedirs(local_repos_dir)
    repo_dir = os.path.join(local_repos_dir, repo)
    # skip if dir already exists.
    if os.path.exists(repo_dir):
        return None

    try:
        with lcd(local_repos_dir):
            if (local('git clone "{0}"'.format(url)).succeeded and
                    os.path.exists(repo_dir)):
                return repo_dir
    except:
        pass
    if os.path.exists(repo_dir):
        shutil.rmtree(repo_dir)
    return None


def git_track_all_branches(repo_dir):
    with lcd(repo_dir):
        get_branches_cmd = (
            'git branch -a | grep remotes | '
            'grep -v HEAD | grep -v master'
        )
        remotes = StringIO.StringIO(local(get_branches_cmd, capture=True))
        for remote in remotes:
            remote = remote.strip()
            track_branch_cmd = 'git branch --track "{0}" "{1}"'.format(
                remote.split('/')[-1],
                remote,
            )
            with settings(warn_only=True):
                local(track_branch_cmd)


def git_push(repo_dir, tar_name, tar_url):
    with lcd(repo_dir):
        names = local('git remote', capture=True)
        if names.find(tar_name) >= 0:
            # todo: add error log
            return False
        local('git remote add {0} "{1}"'.format(tar_name, tar_url))
        return local('git push {0} --all'.format(tar_name)).succeeded
