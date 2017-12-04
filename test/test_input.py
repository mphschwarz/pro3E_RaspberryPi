import unittest
import time

import src.input

class TestCase(unittest.TestCase):
    def test_simon_says_test(self):
        # try:
        #     device = src.input.init_devs('/dev/ttyACM1')
        # except:
        #     device = src.input.init_devs('/dev/ttyACM0')
        device = src.input.init_devs()
        data, previous_index = src.input.request_data(device, 0)
        self.assertFalse(data is None)

    def test_read_stream(self):
        device = src.input.init_devs()
        data = []
        previous_index = 0
        for i in range(0, 10):
            time.sleep(1)
            data_point, previous_index = src.input.request_data(device, previous_index + 1)
            data.append(data_point)
            print(str(data[-1]))
