from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Python library to create a static .html file with text and charts using Google Charts API'

# Setting up
setup(
    name="plot-to-html",
    version=VERSION,
    author="Rafael Rodrigues Troiani",
    author_email="<rafael.r.troiani@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'Google Charts', 'html'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
    ]
)