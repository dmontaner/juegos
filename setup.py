#!/usr/bin/python3
# setup.py
# 2018-01-13 david.montaner@gmail.com
# Games library

from setuptools import setup

setup(
    name='juegos',
    version='0.0.3',
    description='Some educative games',
    long_description='Some educative games I use with my kids.',
    url='https://github.com/dmontaner/juegos',
    author='David Montaner',
    author_email='david.montaner@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='games learning',
    python_requires='>=3',
    scripts=['bin/play-multiplication', 'bin/play-division', 'bin/play-spell'],
    install_requires=['pandas']
)
