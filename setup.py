#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "requests",
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='ocrtool',
    version='0.1.1',
    description="change image to txt with baidu-ocr",
    long_description=readme + '\n\n' + history,
    author="wenjie wu",
    author_email='wuwenjie@gmail.com',
    url='https://github.com/wwj718/ocrtool',
    packages=[
        'ocrtool',
    ],
    package_dir={'ocrtool':
                 'ocrtool'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='ocrtool',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    #scripts = ["ocrtool.ocrtool"]
    entry_points={
         'console_scripts': [
                         'ocrtool = ocrtool.ocrtool:main'
            ]
        },
)
