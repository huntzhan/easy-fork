#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def url_for_gh(user, proj_name):
    '''url example: https://github.com/huntzhan/easy-fork.git
    '''
    if user and proj_name:
        return 'https://github.com/' + user + '/' + proj_name + '.git'
    else:
        return None


def parse_repo_for_gh():
    from config import GITHUB_REPOS
    urls_for_gh = []
    for repo in GITHUB_REPOS:
        if repo.startswith('gh'):
            cont = repo.split(':')[1]
            if cont:
                user, proj_name = cont.split('/')
                url = url_for_gh(user, proj_name)
                urls_for_gh.append(url)

    return urls_for_gh
