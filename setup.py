#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'powo==1.0.0',
    'passlib',
    'python-augeas'
]

test_requirements = [
]

setup(
    name='powo_owinstall',
    version='1.0.1rc',
    description="Open Wide base installation (powo plugin)",
    long_description=readme + '\n\n' + history,
    author="Laurent Almeras",
    author_email='lalmeras@gmail.com',
    url='https://github.com/lalmeras/powo_owinstall',
    packages=[
        'powo_owinstall',
    ],
    package_dir={'powo_owinstall':
                 'powo_owinstall'},
    entry_points={
        'console_scripts': [
            'powo_owinstall=powo_owinstall.cli:main'
        ],
        'powo_plugin': {
            'owinstall=powo_owinstall.plugin:powo_plugin'
        }
    },
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='powo_owinstall',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
