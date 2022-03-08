from setuptools import setup, find_packages

VERSION = "0.0.2"
DESCRIPTION = "Python Module for generating the result of probability based toys."
LONG_DESC = open("README.rst").read()

setup(
    name="pyrandtoys",
    version=VERSION,
    author="thenithinbalaji",
    author_email="thenithinbalaji@outlook.in",
    url="https://github.com/thenithinbalaji/pyrandtoys",
    description=DESCRIPTION,
    long_description=LONG_DESC,
    packages=find_packages(),
    install_requires=[],
    keywords=["python", "random", "probability", "experiment"],
    classifiers=[
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
    ],
)
