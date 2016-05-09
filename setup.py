from setuptools import setup, find_packages
from codecs import open
from os import path
from fileidentify import main

here = path.abspath(path.dirname(__file__))


try:
    long_description = open(path.join(here, 'README.rst'), encoding='utf-8').read()

    setup(
    name='fileidentify',
    version='1.9',
    description='File type identification',
    long_description=long_description,
    url='https://github.com/rida914-4/fileidentify',
    author='ridah',
    author_email='ridah.naseem@ebryx.com',
    license='MIT',
    classifiers=[

    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    ],

    keywords='',
    py_modules=["fileidentify"],
    install_requires=['python-magic==0.4.11'],
    entry_points={
    'console_scripts': [
    'fileidentify=fileidentify:main',
    ],
    },
    )

