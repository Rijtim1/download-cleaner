from setuptools import setup
import py2exe

setup(
    name='download-cleaner',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        '',
    ],
    py_modules=[
        'clean',
    ],
)
