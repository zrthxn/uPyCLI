from setuptools import setup, find_packages

setup(
    name='upycli',
    version='0.1.0',
    packages=find_packages(),
    description='A microscopic library to turn any function into a CLI.',
    entry_points = {
        'console_scripts': ['ucli=upycli.runner:run'],
    }
)
