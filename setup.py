#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='serwersms',
    version='1.1',
    description='Klient Python do komunikacji z API v2 SerwerSMS.pl',
    author='SerwerSMS',
    author_email='biuro@serwersms.pl',
    url='http://serwersms.pl',
    packages=['serwersms'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3.4'
    ]
)
