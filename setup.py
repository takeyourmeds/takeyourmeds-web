#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages

if sys.argv[1:2] == ['test']:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'takeyourmeds.settings')
    from django.core.management import execute_from_command_line
    sys.exit(execute_from_command_line(sys.argv + ['--verbosity=2']))

setup(
    name='takeyourmeds',
    scripts=('takeyourmeds/manage.py',),
    packages=find_packages(),
)
