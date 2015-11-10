from setuptools import setup
from os import path
from io import open


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name="gitgraph",
    version='0.0.0',
    description='',
    long_description=long_description,
    url='https://github.com/reustonium/gitgraph',
    author='Andy Ruestow',
    license='GPLv2',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Version Control',
        'Topic :: Utilities'
    ],
    keywords='git graph cli stats',
    install_requires=[

    ],
)
