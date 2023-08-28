from setuptools import setup, find_packages
from pathlib import Path

def read_requirements():
    return list(Path('requirements.txt').read_text().splitlines())

setup(
    name='uPyCLI',
    version='0.1.0',
    packages=find_packages(),
    install_requires=read_requirements(),
    description='A microscopic library to turn any function into a CLI.',
)