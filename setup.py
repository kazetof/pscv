# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pscv',
    version='0.0.1',
    description='personal computer vision package named pseudo cv',
    long_description=readme,
    author='kazetof',
    author_email='hogehoge',
    install_requires=['numpy'],
    url='hogehoge',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

