from setuptools import setup

setup(
    name="maze",
    author="Ivan Cui"
    version='1.0',
    url="https://github.com/whosivan/LM"
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
