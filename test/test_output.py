import os
import unittest
import random
import math

import src.archive
import src.output


def random_data():
    data = []
    for i in range(0, 100):
        data.append(src.archive.DataPoint(random.uniform(0, 230), random.uniform(0, 13),
                                          random.uniform(0, 230*13), random.uniform(0, 230*13),
                                          random.uniform(0, 60)))
        data[-1].time_stamp += len(data)
    return data


class TestClass(unittest.TestCase):
    def test_generate_plot(self):
        """generates random data and checks if plot exists"""
        data = random_data()
        outfile = src.output.make_plot('../output', data, plot_name='test_plot')
        self.assertTrue(os.path.isfile(outfile))

    def test_generate_html(self):
        """generates random data and checks if html exists"""
        data = random_data()
        outfile = src.output.make_html('../output', data, site_name='test_site', plot_name='test_plot')
        self.assertTrue(os.path.isfile(outfile))
