from setuptools import find_packages, setup

with open("README.md") as filey:
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
    url="https://github.com/vsoch/pokemon",
    license="LICENSE",
    description="ascii database of pokemon... in Python!",
    keywords="pokemon, avatar, ascii, gravatar",
    entry_points={
        "console_scripts": [
            "pokemon=pokemon.scripts:main",
        ],
    },
)
