from setuptools import setup

setup(
    name='gtk3demo',
    version='0.0.1',
    packages=['gtk3demo'],
    install_requires=[
        'requests',
        'python_version >= "3.7"',
    ],

    entry_points={
        'console_scripts': [
            'gtk3-demo-app = gtk3demo.__main__:main'
         ],
    }
)
