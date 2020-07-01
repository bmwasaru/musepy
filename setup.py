from setuptools import setup, find_packages

from muse import __version__

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='muse',
    version=__version__,
    author="Britone Mwasaru",
    author_email="bmwasaru@gmail.com",
    license="Public domain",
    description='Python microframework',
    packages=find_packages(exclude=['demo']),
    install_requires=required,
    keywords='python microframework',
    platforms=["any"]
)
