from setuptools import setup
import unittest

setup(
        name='piapp',
        py_modules=['src.main',
                    'src.archive',
                    'src.output'],
        install_requires=['matplotlib',
                          'pyusb']
)
