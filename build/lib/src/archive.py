import math
import collections
import time
import re

read_reg = '(-?[0-9]+\.?[0-9]+);\s' \
           '(-?[0-9]+\.?[0-9]+),\s' \
           '(-?[0-9]+\.?[0-9]+);\s' \
           '(-?[0-9]+\.?[0-9]+),\s' \
           '(-?[0-9]+\.?[0-9]+),\s' \
           '(-?[0-9]+\.?[0-9]+)'

DataSet = collections.namedtuple('DataSet', ['time_stamp', 'voltage', 'current',
                                             'total_power', 'real_power', 'imag_power'])

class DataPoint:
    """mean data over a measuring period"""

    def __init__(self, volt, amp, total_power, real_power, imag_power, time_stamp=None):
        """
        :param volt: rms value of voltage
        :param amp: rms value of current
        """
        if not time_stamp:
            self.time_stamp = time.time()  # time stamp in unix-time
        self.voltage = volt
        self.current = amp
        self.total_power = total_power
        self.real_power = real_power
        self.imag_power = imag_power

    def __repr__(self):
        return 't:{}; V:{}, I:{}; S: {}, P:{}, Q:{}'.format(self.time_stamp,
                                                            self.voltage, self.current,
                                                            self.total_power, self.real_power, self.imag_power)

    def __str__(self):
        return '{}; {}, {}; {}, {}, {}'.format(self.time_stamp,
                                               self.voltage, self.current,
                                               self.total_power, self.real_power, self.imag_power)


def make_text_file(file_path, data):
    file = open('{}/power_useage_{}'.format(file_path, int(time.time())))
    for point in data:
        file.write(point)
    return file


def read_text_file(file):
    data_points = []
    lines = open(file, 'r').readlines()
    for line in lines:
        time_stamp, voltage, current, total_power, real_power, imag_power = re.findall(read_reg, line)[0]
        data_points.append(DataPoint(float(voltage), float(current),
                                     float(total_power), float(real_power), float(imag_power),
                                     time_stamp=float(time_stamp)))

def read_data_set(file):
    data_set = DataSet([], [], [], [], [], [])
    lines = open(file, 'r').readlines()
    for line in lines:
        time_stamp, voltage, current, total_power, real_power, imag_power = re.findall(read_reg, line)[0]
        data_set.time_stamp.append(float(time_stamp))
        data_set.voltage.append(float(voltage))
        data_set.current.append(float(current))
        data_set.total_power.append(float(total_power))
        data_set.real_power.append(float(real_power))
        data_set.imag_power.append(float(imag_power))
    return data_set
