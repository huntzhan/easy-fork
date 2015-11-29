#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import requests


def search_repos(language, stars_lower_bound='*', stars_upper_bound='*'):
    url_template = 'https://api.github.com/search/repositories?q={0}&{1}'
    q_template = 'language:"{0}" stars:"{1} ... {2}"'
    page_parameters = 'page={0}&per_page=100'

    items = []
    page_num = 1
    while True:
        url = url_template.format(
            q_template.format(language, stars_lower_bound, stars_upper_bound),
            page_parameters.format(page_num),
        )
        print(url)
        json_body = requests.get(url).json()

        ITEMS_KEY = 'items'
        if ITEMS_KEY not in json_body:
            break
        if len(json_body[ITEMS_KEY]) == 0:
            break

        items.extend(json_body[ITEMS_KEY])
        page_num += 1
    return items
