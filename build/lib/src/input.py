import click
import serial
import time
import re

import src


def init_devs(dev_name=None, boud=115200, timeout=0.1):
    """:returns pointer to serial device"""
    if not dev_name:
        # TODO test devices systematically
        try:
            return serial.Serial('/dev/ttyACM0', boud, timeout=timeout)
        except serial.serialutil.SerialException:
            return serial.Serial('/dev/ttyACM1', boud, timeout=timeout)
    else:
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


def request_data(device, previous_index, debug=False):
    """
    :param device: already set up serial device
    :param previous_index: index of previous message, to prevent multiple reading of the same sample
    :param debug: prints ingested sample data
    :returns reads data from serial device"""
    regex = r'(-?[0-9]+\.[0-9]+),\s(-?[0-9]+\.[0-9]+);\s(-?[0-9]+\.[0-9]+),\s(-?[0-9]+\.[0-9]+),\s(-?[0-9]+\.[0-9]+):\s([0-9]+)\\n'
    line = str(device.readline())
    while not re.findall(regex, line) \
            or int(re.findall(regex, line)[0][5]) == previous_index:
            # or int(re.findall(regex, line)[0][5]) != 0:
        # or int(re.findall(regex, line)[0][5]) < previous_index \
        try:
            line = str(device.readline())
        except:
            time.sleep(0.000001)

    data = re.findall(regex, line)
    if data != []:
        if debug:
            click.echo('index: {}, V: {}, I: {}, S: {}, P: {}, Q: {}'.format(previous_index, data[0][0], data[0][1],
                                                                             data[0][2], data[0][3], data[0][4]))
        return src.DataPoint(data[0][0], data[0][1], data[0][2], data[0][3], data[0][4]), int(data[0][-1])
    else:
        return None
