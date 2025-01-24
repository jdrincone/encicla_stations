from setuptools import setup, find_packages

setup(
    name="encicla_stations",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "pandas>=2.0.3",
    ],
)