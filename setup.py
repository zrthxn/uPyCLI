from setuptools import setup, find_packages

with open("README.md", "r") as f:
    README = f.read()

setup(
    name='upycli',
    version='0.1.0',
    packages=find_packages(),
    description='A microscopic library to turn any function into a CLI.',
    long_description=README,
    entry_points = {
        'console_scripts': ['ucli=upycli.runner:run'],
    }
)
