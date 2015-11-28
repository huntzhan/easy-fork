#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
from docopt import docopt

from easy_fork.file_operators.gitlab_config import load_gitlab_config
from easy_fork.file_operators.repo_config import load_repo_config
from easy_fork.git_repo_operations.git_repo_operator import (
    git_clone_to_dir,
    git_track_all_branches,
    git_push,
)
from easy_fork.gitlab_operations.project import GitLabProjectAPIHandler


CLI_DOC = '''
Usage:
    easy-fork --gitlab-config <gitlab_config_path>
              --repo-config <repo_config_path>
'''


def entry_point():
    args = docopt(CLI_DOC)
    gitlab_config = load_gitlab_config(args['--gitlab-config'])
    repo_ids = load_repo_config(args['--repo-config'])

    gitlab_project_handler = GitLabProjectAPIHandler(gitlab_config)

    local_repos_dir = os.getcwd()
    for repo_id in repo_ids:
        # download.
        repo_dir = git_clone_to_dir(
            repo_id.repo,
            repo_id.url,
            local_repos_dir,
        )
        # create project in gitlab.
        remote_url = gitlab_project_handler.create_project(repo_id)
        # configure local git repo and push.
        git_track_all_branches(repo_dir)
        git_push(repo_dir, 'git-oa', remote_url)
