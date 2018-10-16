#!/usr/bin/env python

from setuptools import setup
from setuptools.config import read_configuration

import os

setup(**read_configuration(os.path.join(
    os.path.dirname(__file__), 'setup.cfg'))['options'])
