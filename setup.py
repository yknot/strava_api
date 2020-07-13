#!/usr/bin/env python

from setuptools import setup, find_packages  # type: ignore

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Andrew Yale",
    author_email="a.yale9@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="A python library for working with the Strava API",
    install_requires=[],
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={"strava_api": ["py.typed"]},
    include_package_data=True,
    keywords="strava_api",
    name="strava_api",
    package_dir={"": "src"},
    packages=find_packages(include=["src/strava_api", "src/strava_api.*"]),
    setup_requires=[],
    url="https://github.com/yknot/strava_api",
    version="0.1.0",
    zip_safe=False,
)
