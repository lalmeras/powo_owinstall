# -*- coding: utf-8 -*-

import glob
import os.path
import pkg_resources

import powo.model


def powo_plugin():
    roles_path = pkg_resources.resource_filename(__name__, 'ansible/roles')
    playbooks_path = \
        pkg_resources.resource_filename(__name__, 'ansible/playbooks')
    pkg_resources.resource_filename(__name__, 'ansible/playbooks/vars')
    playbooks = []
    for f in glob.glob(os.path.join(playbooks_path, '*.yml')):
        playbooks.append(f)
    return powo.model.PowoPlugin(
        roles_path=roles_path,
        playbooks=playbooks,
        galaxy_roles=['paluh.augeas', 'cchurch.virtualenv']
    )
