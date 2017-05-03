from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='currency-converter',

    version='1.0.0',

    description='Simple currency converter with json output',
    long_description=long_description,

    url='',

    author='Tibor Mikita',
    author_email='tibor@mikita.eu',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7'
    ],

    keywords='currency conversion money util online latest rates',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['forex-python>=0.3.2'],

    entry_points={
        'console_scripts': [
            'currency-converter=currency_converter:main',
        ],
    },
)
