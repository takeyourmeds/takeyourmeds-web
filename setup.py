#!/usr/bin/env python

import os

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

setup(
    name='takeyourmeds',
    scripts=('takeyourmeds/manage.py',),
    packages=find_packages(),
    zip_safe=False,
    data_files=find_data_files(('static', 'templates')),
    test_suite='setuptest.setuptest.SetupTestSuite',
)
