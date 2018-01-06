import os
import unittest
import random
import math

# import src.archive
import src.output


def random_data():
    data = []
    for i in range(0, 100):
        data.append(src.DataPoint(random.uniform(0, 230), random.uniform(0, 13),
                                  random.uniform(0, 230 * 13),
                                  random.uniform(0, 230 * 13),
                                  random.uniform(0, 230 * 13),
                                  time_stamp=i))
        # data[-1].time_stamp += len(data)
    return data


class TestClass(unittest.TestCase):
    def test_generate_plot(self):
        """generates random data and checks if plot exists"""
        data = random_data()
        outfile = src.output.make_plot(src.DataSet([float(data_point.time_stamp) for data_point in data],
                                                   [float(data_point.voltage) for data_point in data],
                                                   [float(data_point.current) for data_point in data],
                                                   [float(data_point.total_power) for data_point in data],
                                                   [float(data_point.real_power) for data_point in data],
                                                   [float(data_point.imag_power) for data_point in data]),
                                       '../output', plot_name='test_plot')
        self.assertTrue(os.path.isfile(outfile))

    def test_generate_html(self):
        """generates random data and checks if html exists"""
        data = random_data()
        outfile = src.output.make_html('../output', '../output/latest.png', '../output/total.png',
                                       site_name='test_site')
        self.assertTrue(os.path.isfile(outfile))

    def test_make_table(self):
        path = '../output'
        print(src.output.make_table(path))
