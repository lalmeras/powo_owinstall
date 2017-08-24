# -*- coding: utf-8 -*-

import glob
import pwd
import os.path
import pkg_resources
import re
import sys

import powo.model
import click


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
        galaxy_roles=['paluh.augeas', 'cchurch.virtualenv'],
        on_run=on_run,
        decorate_update=decorate_update
    )


def on_run(ctx, extra_vars):
    no_user = ctx.params['no_user']
    powo_user = None

    if not no_user:
        if ctx.params['ow_username']:
            powo_user = ctx.params['ow_username']
        elif extra_vars['ow_username']:
            powo_user = extra_vars['ow_username']

        # enforce valid username
        while not no_user and not validate_username(powo_user):
            if not sys.stdin.isatty():
                raise click.ClickException('powo_user not found and terminal '
                                           'is not interactive')
            powo_user = \
                click.prompt('Please provide a valid username ; '
                             'this user will be created if missing',
                             type=click.STRING)

        extra_vars['powo_user'] = powo_user
        extra_vars['powo_home'] = '/home/%s' % (powo_user)
        pass_needed = True
        if powo_user is not None:
            try:
                pwd.getpwnam(powo_user)
                pass_needed = False
            except KeyError:
                pass
        if not no_user and pass_needed:
            powo_password = None
            if not no_user and not powo_password:
                if not sys.stdin.isatty():
                    raise click.ClickException(
                        'powo_password not found and terminal'
                        'is not interactive')
                powo_password = \
                    click.prompt(
                        'Please provide a password for user %s'
                        % (powo_user),
                        type=click.STRING, hide_input=True,
                        confirmation_prompt=True)
                extra_vars['powo_password'] = powo_password
        if ctx.params['ow_fullname']:
            extra_vars['powo_fullname'] = ctx.params['ow_fullname']
        elif 'ow_fullname' in extra_vars and extra_vars['ow_fullname']:
            extra_vars['powo_fullname'] = extra_vars['ow_fullname']

        if ctx.params['ow_group']:
            extra_vars['powo_group'] = ctx.params['ow_group']
        elif 'ow_group' in extra_vars and extra_vars['ow_group']:
            extra_vars['powo_group'] = extra_vars['ow_group']

        if ctx.params['ow_ask_ssh_passphrase']:
            if not sys.stdin.isatty():
                raise click.ClickException(
                    'powo_passphrase not found and terminal '
                    'is not interactive')
            powo_passphrase = \
                click.prompt(
                    'Please provide a passphrase for user %s''s ssh key'
                    % (powo_user),
                    type=click.STRING, hide_input=True,
                    confirmation_prompt=True)
            extra_vars['powo_passphrase'] =  powo_passphrase


def get_var(templar, vars, name):
    var = vars.get(name)
    if var is None:
        return var
    return templar.template(var)


def validate_username(username):
    if username is None:
        return False
    if re.match(r'^[a-z0-9_-]{3,15}$', username):
        return True
    return False


def _update_extra_vars(variable_manager, key, value):
    updated_orig = variable_manager.extra_vars
    updated_orig.update({key: value})
    variable_manager.extra_vars = updated_orig


def decorate_update(update):
    click.option('--no-user', is_flag=True,
                 help='no user account is needed')(update)
    click.option('--ow-username', default=None,
                 help='user account to manage (default from configuration file)'
                 )(update)
    click.option('--ow-group', default=None,
                 help='user group (used for files'' mode, username by default)'
                 )(update)
    click.option('--ow-fullname', default=None,
                 help='user full name'
                 )(update)
    click.option('--ow-ask-ssh-passphrase', is_flag=True, default=False,
                 help='ssh key passphrase (only for generation)'
                 )(update)
