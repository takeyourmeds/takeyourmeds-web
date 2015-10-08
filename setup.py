#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages

NAME = 'takeyourmeds'

DATA = (
    'static',
    'templates',
)

if sys.argv[1:2] == ['test']:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '%s.settings' % NAME)
    from django.core.management import execute_from_command_line
    sys.exit(execute_from_command_line(sys.argv))

def find_data(dirs):
    result = []
    for x in dirs:
        for y, _, _ in os.walk(x):
            result.append(os.path.join(y, '*'))
    return result

setup(
    name=NAME,
    scripts=('%s/manage.py' % NAME,),
    packages=find_packages(),
    package_data={NAME: find_data(DATA)},
)
