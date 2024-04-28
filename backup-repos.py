#!/usr/bin/env python3

# Copyright 2022 Vulcalien
#
# License: http://creativecommons.org/publicdomain/zero/1.0/
# To the extent possible under law, Vulcalien has waived all
# copyright and related or neighboring rights to this work.
#
# Backup all public repositories for a GitHub user.
# By default, forks are skipped.

import json, os

from urllib.request import urlopen

USER = ''

os.chdir(os.path.dirname(__file__))

with urlopen('https://api.github.com/users/' + USER + '/repos') as f:
    repos_list = json.loads(f.read())

for repo in repos_list:
    print('\033[31m' + repo['name'] + '\033[m')
    if repo['fork']:
        print('Fork: skipping')
        continue

    if not os.path.exists(repo['name'] + '.git'):
        os.system('git clone --mirror -- "' + repo['clone_url'] + '"')
    else:
        os.chdir(repo['name'] + '.git')
        os.system('git remote update')
        os.chdir('..')
