from setuptools import setup

setup(
    name="recengine",
    version="0.1",
    py_modules=["cli"],
    install_requires=[
        "Click",
    ],
    entry_points='''
        [console_scripts]
        recengine=cli:cli
    ''',
)
