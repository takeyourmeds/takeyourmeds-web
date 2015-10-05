#!/usr/bin/env python

import os
import setuptools

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

setuptools.setup(
    name=NAME,
    scripts=('%s/manage.py' % NAME,),
    packages=(NAME,),
    package_data={NAME: find_data(DATA)},
)
