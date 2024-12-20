#!/usr/bin/env python
import os.path
import io
from setuptools import setup, find_packages


setup(
    name="zerotk.url2env",
    version="1.3.8",
    author="Alexandre Andrade",
    author_email="kaniabi@gmail.com",
    url="https://github.com/zerotk/url2env",
    description="Produces env vars from Heroku-style database URLs",
    long_description_content_type="text/markdown",
    long_description=io.open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"),
        encoding="utf-8",
    ).read(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    keywords="postgresql shell environment",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    py_modules=["url2env"],
    entry_points={
        "console_scripts": ["url2env=url2env:main"],
    },
    install_requires=[
        "click",
    ],
    setup_requires=[],
    tests_require=[],
    license="MIT",
)
