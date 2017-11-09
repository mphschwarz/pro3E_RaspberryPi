import serial
import time

def init_devs(dev_name='/dev/ttyACM0', boud=115200, timeout=0.1):
    """:returns pointer to serial device"""
    return serial.Serial(dev_name, boud, timeout=timeout)

def request_value(device, value):
    """:param device: pointer to serial device
    :param value: u, i, p, q, x for voltage, current, real- and imag power, x for test
    :returns measured value"""
    device.write(bytes(value, 'utf-8'))
    time.sleep(0.001)
    data = device.readline()
    if data:
        return data
    else:
        return None

