#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import requests

from easy_fork.gitlab_operations.utils import (
    GitLabRESTfulURL,
    get_project_name,
    get_namespace_project_name,
)


class GitLabProjectAPIHandler(GitLabRESTfulURL):

    def __init__(self, *args, **kwargs):
        super(GitLabProjectAPIHandler, self).__init__(*args, **kwargs)
        # get namespace_id.
        self.namespace_id = self.get_namespace_id()

    # return a string for `git remote add` operation.
    def create_project(self, repo_id):
        success, url = self.check_exitences(repo_id)
        if not success:
            self.post_project(repo_id)
        success, url = self.check_exitences(repo_id)
        assert success
        return url

    def check_exitences(self, repo_id):
        namespace_project_name = get_namespace_project_name(
            self.namespace_id,
            get_project_name(repo_id.owner, repo_id.repo),
        )

        url = self.url_template.format(
            '/projects/{0}'.format(namespace_project_name),
        )
        response = requests.get(url)
        if response.status_code == 404:
            return False, None
        else:
            response_json = response.json()
            return True, self.attach_auth_info(
                response_json['http_url_to_repo'],
            )

    def post_project(self, repo_id):
        body = {
            'name': get_project_name(repo_id.owner, repo_id.repo),
            'namespace_id': self.namespace_id,
        }
        url = self.url_template.format('/projects')
        response = requests.post(url, json=body)
        assert response.status_code == 200

    def get_namespace_id(self):
        url = self.url_template.format(
            '/groups/{0}'.format(self.gitlab_config.groupname),
        )
        response = requests.get(url)
        assert response.status_code == 200
        return response.json()['id']
