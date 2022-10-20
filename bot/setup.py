from setuptools import setup, find_packages

setup(
    name="archivebot",
    version="0.1.0",
    packages=find_packages(),
    scripts=["src/bin/archive-bot"],
)
