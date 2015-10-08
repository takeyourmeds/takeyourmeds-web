#!/usr/bin/env python

import os

from setuptools import setup, find_packages

NAME = 'takeyourmeds'

DATA = (
    'static',
    'templates',
)

def find_data(dirs):
    result = []
    for x in dirs:
        for y, _, _ in os.walk(x):
            result.append(os.path.join(y, '*'))
    return result

setup(
    name=NAME,
    scripts=('%s/manage.py' % NAME,),
    test_suite='setuptest.setuptest.SetupTestSuite',
    packages=find_packages(),
    package_data={NAME: find_data(DATA)},
    tests_require=(
        'django-setuptest',
    ),
)
