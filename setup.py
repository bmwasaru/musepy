import os
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='musepy',
    version='0.1',
    description='Python microframework',
    packages=find_packages(exclude=['demo']),
    install_requires=required,
    keywords='python microframework'
)
