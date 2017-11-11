from setuptools import setup

setup(
    name="maze",
    version='1.0',
    py_modules=['lasermaze'],
    install_requires=[
        'Click',
        'numpy',
        'pandas',
    ],
    entry_points='''
        [console_scripts]
        maze=lasermaze:LaserMaze
    ''',
)
