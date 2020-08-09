from setuptools import setup, find_packages

setup(
    name="Ligabot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'lxml'
    ],
    tests_require=['pytest'],
)
