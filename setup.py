from setuptools import setup, find_packages

setup(
    name='Oasis_Bot',
    version='0.1',
    packages=find_packages(),
    description='Implementacion Bot de Discord',
    install_requires=[
        'discord',
        'dotenv',
    ],
)
