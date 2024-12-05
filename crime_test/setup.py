from setuptools import setup, find_packages

setup(
    name='crime_test',
    version="3.12.7',
    packages=find_packages(),
    install_requires=[
        "pandas",
        "pytest",
    ],
    author="Deema Saddik",
    description="A package to validate and analyze crime data",
    author_email='deema.saddik@sjsu.edu',
    url='https://github.com/deemasaddik/crime_test', #Optional
)
