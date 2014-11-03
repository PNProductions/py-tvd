#!/usr/bin/env python

from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='py-tvd',
      version='1.0',
      description='A total variation denoising implementation in python.',
      author='Piero Dotti, Paolo Guglielmini',
      author_email='pnproductions.dev@gmail.com',
      url='https://github.com/PNProductions/py-tvd',
      packages=['tvd'],
      install_requires=requirements,
      setup_requires=requirements
      )
