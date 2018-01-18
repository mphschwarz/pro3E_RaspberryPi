from setuptools import setup
import unittest
# Raspi wifi config:
# ssid: WiPi
# pw: raspberry
#
# Raspi ssh config:
# login: pi
# pw: blackberry
#
# Raspi website config:
# url: 129.168.42.1

setup(
        name='piapp',
        py_modules=['src.main',
                    'src.output',
                    'src.input'],
        install_requires=['matplotlib',
                          'click',
                          'pyusb',
                          'pycairo',
                          'cairocffi'],
        entry_points={
            'console_scripts': [
                'piapp=src.main:main',
            ],
        },
)
