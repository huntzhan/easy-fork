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


GitLabConfig = namedtuple(
    'GitLabConfig',
    ['api_prefix', 'username', 'password', 'token'],
)


def load_gitlab_config(gitlab_config_path):
    gitlab_config = imp.load_source('gitlab_config', gitlab_config_path)
    keys = [API_PREFIX, USERNAME, PASSWORD, TOKEN]
    return GitLabConfig(
        api_prefix=getattr(gitlab_config, API_PREFIX),
        username=getattr(gitlab_config, USERNAME),
        password=getattr(gitlab_config, PASSWORD),
        token=getattr(gitlab_config, TOKEN),
    )
