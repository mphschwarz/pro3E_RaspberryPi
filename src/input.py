import serial
import time

import src.archive


def init_devs(dev_name='/dev/ttyACM0', boud=115200, timeout=0.1):
    """:returns pointer to serial device"""
    return serial.Serial(dev_name, boud, timeout=timeout)


def request_value(device, value):
    """requests voltage or current or real power or imag power or dummy response over serial connection
    :param device: pointer to serial device
    :param value: u -> voltage, i -> current, p -> real power, q -> imag power, x -> test response
    :returns measured value"""
    device.write(bytes(value, 'utf-8'))
    time.sleep(0.001)
    data = device.readline()
    if data:
        return data
    else:
        return None


def request_full_data(device):
    """:returns a single Data Point"""
    return src.archive.DataPoint(request_value(device, 'u'),
                                 request_value(device, 'i'),
                                 request_value(device, 'p'),
                                 request_value(device, 'q'))
