#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from easy_fork.file_operators.gitlab_config import GitLabConfig
from easy_fork.gitlab_operations.utils import GitLabRESTfulURL


def tet_url_template():
    gitlab_config = GitLabConfig(
        api_prefix='http://gitlab.com/api/v3/',
        username='',
        password='',
        token='Fapjifjea21',
        groupname='',
    )
    obj = GitLabRESTfulURL(gitlab_config)
    assert ('http://gitlab.com/api/v3/{0}?private_token=Fapjifjea21' ==
            obj.url_template)
