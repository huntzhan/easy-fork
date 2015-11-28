#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from easy_fork.file_operators.gitlab_config import GitLabConfig
from easy_fork.gitlab_operations.utils import GitLabRESTfulURL


gitlab_config = GitLabConfig(
    api_prefix='http://gitlab.com/api/v3/',
    username='testuser',
    password='testpassword',
    token='Fapjifjea21',
    groupname='testgroup',
)


def test_url_template():
    obj = GitLabRESTfulURL(gitlab_config)
    assert ('http://gitlab.com/api/v3/{0}?private_token=Fapjifjea21' ==
            obj.url_template)


def test_attach_auth_info():
    obj = GitLabRESTfulURL(gitlab_config)
    assert ('http://testuser:testpassword@abc' ==
            obj.attach_auth_info('http://abc'))
