from setuptools import setup
from setuptools.dist import Distribution
from os import path

__dir__ = path.abspath(path.dirname(__file__))
readme_path = path.join(__dir__, 'README.md')

with open(readme_path, encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name='wasmer',
    version='1.2.0',
    author='The Wasmer Engineering Team',
    author_email='engineering@wasmer.io',
    license='MIT',
    packages=['wasmer'],
    description='Python extension to run WebAssembly binaries',
    long_description=long_description,
    long_description_content_type='text/markdown',
    zip_safe=False,
    platforms='any',
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
