#!/usr/bin/env python

# Copyright 2018 Red Hat Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

# Version reading from yacfg/meta.py
# according to (3b) from:
# https://packaging.python.org/guides/single-sourcing-package-version/
meta = {}
with open('src/yacfg/meta.py', 'r') as meta_file:
    exec(meta_file.read(), meta)

setup(
    name=meta.get('NAME'),
    version=meta.get('VERSION'),
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'yacfg = yacfg.yacfg_cli:main',
            'yacfg-batch = yacfg_batch.yacfg_batch_cli:main'
        ],
    },
    install_requires=[
        'jinja2',
        'pyyaml',
    ],
    extras_require={
        'color_log': ['colorama', 'colorlog']
    },
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest',
        'mock',
    ],
    url='https://github.com/rh-messaging-qe/yacfg',
    license='Apache-2.0',
    author='Zdenek Kraus',
    author_email='zkraus@redhat.com',
    maintainer="Dominik Lenoch",
    maintainer_email="dlenoch@redhat.com",
    description=meta.get('SHORT_DESCRIPTION'),
    long_description=meta.get('DESCRIPTION'),
    include_package_data=True,
    # package_data={'yacfg': ['src/yacfg/profiles/*/*', 'src/yacfg/templates/*/*'']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Systems Administration',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ],
)
