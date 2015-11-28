#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
# example:
#
# REPO_IDS = [
#     'gh:huntzhan/easy-fork',
#     'gh:JanFan/JanC-Language-Interpreter',
# ]
#
# repo identifier would be transfromed to a namedtuple, with following format:
#
#     namedtuple(<repo-identifier-type>, ['repo_identifier_type', *parameters])
#
# where <repo-identifier-type> represents the **type** of repo identifier, and
# the form of parameters depends on <repo-identifier-type>.
#
# demo version only supports github repo identifier.
#
# 'gh:owner/repo' would be transfromed to following namedtuple:
#
#     namedtuple(REPO_ID_TYPE_GITHUB,
#                ['repo_identifier_type', 'owner', 'repo'])

from collections import namedtuple
import imp


REPO_ID_TYPE_GITHUB = 'GitHubRepoID'

GitHubRepoID = namedtuple(
    REPO_ID_TYPE_GITHUB,
    ['repo_id_type', 'owner', 'repo', 'fullname', 'url'],
)


REPO_IDS = 'REPO_IDS'


def load_repo_config(repo_config_path):
    repo_config = imp.load_source('repo_config', repo_config_path)

    repo_ids = []
    for raw_repo_id in getattr(repo_config, REPO_IDS, []):
        if raw_repo_id.startswith('gh:'):
            component = raw_repo_id[3:].strip().split('/')

            # prepare parameters.
            owner = component[0]
            repo = component[1]
            fullname = '{0}/{1}'.format(owner, repo)
            url = 'https://github.com/{0}/{1}.git'.format(owner, repo)

            repo_ids.append(
                GitHubRepoID(REPO_ID_TYPE_GITHUB, owner, repo, fullname, url),
            )

    return repo_ids
