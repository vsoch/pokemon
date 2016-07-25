from setuptools import setup, find_packages
import codecs
import os

setup(
    # Application name:
    name="pokemon",

    # Version number:
    version="0.2",

    # Application author details:
    author="Vanessa Sochat",
    author_email="vsochat@stanford.edu",

    # Packages
    packages=find_packages(),

    # Data files
    include_package_data=True,
    zip_safe=False,

    # Details
    url="http://www.github.com/vsoch/pokemon-ascii",

    license="LICENSE",
    description="ascii database of pokemon... in python!",
    keywords='pokemon, avatar, ascii, gravatar',

    install_requires = ['numpy'],

    entry_points = {
        'console_scripts': [
            'pokemon=pokemon.scripts:main',
        ],
    },

)
