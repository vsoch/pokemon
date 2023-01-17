from setuptools import setup, find_packages
import os

with open('README.md') as filey:
    LONG_DESCRIPTION = filey.read()

setup(
    # Application name:
    name="pokemon",

    # Version number:
    version="0.36",

    # Application author details:
    author="Vanessa Sochat",
    author_email="vsoch@noreply.github.users.com",

    # Packages
    packages=find_packages(),

    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",

    # Data files
    include_package_data=True,
    zip_safe=False,

    # Details
    url="http://www.github.com/vsoch/pokemon",
    license="LICENSE",
    install_requires=['Pillow'],
    description="ascii database of pokemon... in python!",
    keywords="pokemon, avatar, ascii, gravatar",
    entry_points={"console_scripts": ["pokemon=pokemon.scripts:main",],},
)
