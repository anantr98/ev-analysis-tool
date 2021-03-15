import os
from setuptools import setup, find_packages

PACKAGES = find_packages()

setup(
    name='EVAnalysis',
    version='0.1',
    packages=PACKAGES,
    url='https://github.com/anantr98/ev-analysis-tool',
    license='',
    author=['Anant Rajeev', 'Leena Elamrawy', 'Krisha Mehta'],
    package_data={'EVAnalysis': ['data/*']},
    author_email='kkm98@uw.edu, anantr@uw.edu, lelamraw@uw.edu',
    description='An Analysis tool for EVs'
)
