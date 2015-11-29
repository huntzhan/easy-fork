#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from easy_fork.file_operators.gitlab_config import GitLabConfig
from easy_fork.gitlab_operations.utils import (
    GitLabRESTfulURL,
    get_project_name,
)


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


def test_get_project_name():
    assert ('gh-vundlevim-vundle-vim' ==
            get_project_name('VundleVim', 'Vundle.vim'))

    assert ('gh-a-b-c' ==
            get_project_name('a-------b', '------#@(----c'))
