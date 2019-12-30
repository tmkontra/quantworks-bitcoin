from setuptools import setup, find_namespace_packages

setup(
    name='quantworks-bitcoin',
    version='0.0.1.dev1',
    packages=find_namespace_packages(include=["quantworks.ext.*"]),
    install_requires=[
      'quantworks',
      'six',
      'requests'
    ],
)