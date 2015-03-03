### "Whole"
from setuptools import setup, find_packages

setup(
    name = "ValueMaths",
    version = "0.1",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/valuemath'],
    install_requires = []
)
