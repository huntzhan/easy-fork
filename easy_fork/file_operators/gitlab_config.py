#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import imp
from collections import namedtuple


API_PREFIX = 'GITLAB_API_PREFIX'
USERNAME = 'EASYFORK_GITLAB_USERNAME'
PASSWORD = 'EASYFORK_GITLAB_PASSWORD'
TOKEN = 'EASYFORK_GITLAB_TOKEN'
GROUPNAME = 'EASYFORK_GITLAB_GROUPNAME'
GROUPID = 'EASYFORK_GITLAB_GROUPID'


GitLabConfig = namedtuple(
    'GitLabConfig',
    ['api_prefix', 'username', 'password', 'token', 'groupname', 'groupid'],
)


def load_gitlab_config(gitlab_config_path):
    gitlab_config = imp.load_source('gitlab_config', gitlab_config_path)

    api_prefix = getattr(gitlab_config, API_PREFIX)
    api_prefix = api_prefix.rstrip('/')

    return GitLabConfig(
        api_prefix=api_prefix,
        username=getattr(gitlab_config, USERNAME),
        password=getattr(gitlab_config, PASSWORD),
        token=getattr(gitlab_config, TOKEN),
        groupname=getattr(gitlab_config, GROUPNAME),
        groupid=getattr(gitlab_config, GROUPID),
    )
