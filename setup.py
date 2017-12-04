from setuptools import setup
import unittest

# Raspi WiFi config:
# ssid: WiPi
# pw: raspberry
# ip: 129.168.42.1

setup(
        name='piapp',
        py_modules=['src.main',
                    'src.archive',
                    'src.output',
                    'src.input'],
        install_requires=['matplotlib',
                          'click',
                          'pyusb'],
        entry_points={
            'console_scripts': [
                'piapp=src.main:main',
            ],
        },
)
