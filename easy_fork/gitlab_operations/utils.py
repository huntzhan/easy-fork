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
