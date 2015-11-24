#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages

def find_data_files(dirs):
    result = []
    for x in dirs:
        for dirpath, _, filenames in os.walk(x):
            result.append((
                dirpath,
                [os.path.join(dirpath, y) for y in filenames],
            ))
    return result

if sys.argv[1:2] == ['test']:
    # Monkey patch https://github.com/praekelt/django-setuptest/pull/26
    import importlib
    sys.modules['django.utils.importlib'] = importlib

setup(
    name='takeyourmeds',
    scripts=('takeyourmeds/manage.py',),
    packages=find_packages(),
    zip_safe=False,
    data_files=find_data_files(('media', 'templates')),
    test_suite='setuptest.setuptest.SetupTestSuite',
)
