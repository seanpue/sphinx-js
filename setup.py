# -*- coding: utf-8 -*-
from io import open
from setuptools import setup, find_packages


setup(
    name='sphinx-js',
    version='2.8',
    description='Support for using Sphinx on JSDoc-documented JS code',
    long_description=open('README.rst', 'r', encoding='utf8').read(),
    long_description_content_type="text/x-rst",
    author='Erik Rose',
    author_email='erikrose@grinchcentral.com',
    license='MIT',
    packages=find_packages(exclude=['ez_setup']),
    url='https://github.com/mozilla/sphinx-js',
    include_package_data=True,
    install_requires=['docutils', 'Jinja2>2.0,<3.0', 'parsimonious>=0.7.0,<0.8.0', 'six>=1.9.0,<2.0', 'Sphinx>=1.6,<3.0'],
    python_requires='>=2.7,!=3.1,!=3.2,!=3.3,!=3.4,!=3.5',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation'
        ],
    keywords=['sphinx', 'documentation', 'docs', 'javascript', 'js', 'jsdoc', 'restructured', 'typescript', 'typedoc'],
)
