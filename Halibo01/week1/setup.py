from setuptools import setup, find_packages

setup(
    name="myproject",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'torch',
    ],
    extras_require={
        'gpu': ['torch==2.0.1+cu118'],
        'cpu': ['torch==2.0.1'],
    },
)