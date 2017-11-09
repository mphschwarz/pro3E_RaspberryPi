import math
import time


class DataPoint:
    """mean data over a measuring period"""

    def __init__(self, volt, amp, real_power, imag_power):
        """
        :param volt: rms value of voltage
        :param amp: rms value of current
        """
        self.time_stamp = time.time()  # time stamp in unix-time
        self.voltage = volt
        self.currant = amp
        self.real_power = real_power
        self.imag_power = imag_power

    def __repr__(self):
        return 't:{}; V:{}, I:{}; P:{}, Q:{}'.format(self.time_stamp,
                                                     self.voltage, self.currant,
                                                     self.real_power, self.imag_power)

    def __str__(self):
        return '{}; {}, {}; {}, {}'.format(self.time_stamp,
                                           self.voltage, self.currant,
                                           self.real_power, self.imag_power)


def make_text_file(file_path, data):
    file = open('{}/power_useage_{}'.format(file_path, int(time.time())))
    for point in data:
        file.write(point)
    return file
