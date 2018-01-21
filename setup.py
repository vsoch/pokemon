from setuptools import setup, find_packages
import os

setup(
    # Application name:
    name="pokemon",

    # Version number:
    version="0.34",

    # Application author details:
    author="Vanessa Sochat",
    author_email="vsochat@stanford.edu",

    # Packages
    packages=find_packages(),

    # Data files
    include_package_data=True,
    zip_safe=False,

    # Details
    url="http://www.github.com/vsoch/pokemon",

    license="LICENSE",
    description="ascii database of pokemon... in python!",
    keywords='pokemon, avatar, ascii, gravatar',

    entry_points = {
        'console_scripts': [
            'pokemon=pokemon.scripts:main',
        ],
    },

)
