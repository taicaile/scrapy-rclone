"""setup"""

import io

from setuptools import find_packages, setup


def read_file(filename):
    """read file content"""
    with io.open(filename, encoding="utf-8") as fp:
        return fp.read().strip()


def read_requirements(filename):
    """read requirements"""
    return [
        line.strip()
        for line in read_file(filename).splitlines()
        if not line.startswith("#")
    ]


setup(
    name="scrapy-rclone",
    version="0.1.0",
    description="MongoDB-based components for Scrapy",
    long_description=read_file("README.md"),
    author="taicaile",
    url="https://github.com/taicaile/scrapy-rclone",
    packages=find_packages(),
    install_requires=read_requirements("requirements.txt"),
    dependency_links=["https://github.com/taicaile/repo/pyrclone/master@v0.1.0"],
)
