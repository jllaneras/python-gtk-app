from setuptools import setup

setup(
    name='gtk3demo',
    version='0.0.1',
    packages=['gtk3demo'],
    install_requires=[
        'requests',
        'importlib; python_version >= "3.7"',
    ],
)
