#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


class GitLabRESTfulURL(object):

    def __init__(self, gitlab_config):
        self.gitlab_config = gitlab_config

    @property
    def url_template(self):
        return (
            self.gitlab_config.api_prefix +
            '{0}' +
            '?private_token=' +
            self.gitlab_config.token
        )

    def attach_auth_info(self, url):
        assert url.startswith('http://')
        auto_info = 'http://{0}:{1}@'.format(
            self.gitlab_config.username,
            self.gitlab_config.password,
        )
        return auto_info + url[7:]


def get_project_name(owner, repo):
    # return '{0}--{1}'.format(owner, repo)
    repo = repo.replace('.', '-')
    repo = repo.lower()
    return repo


def get_namespace_project_name(namespace_name, project_name):
    return '{0}%2F{1}'.format(namespace_name, project_name)
