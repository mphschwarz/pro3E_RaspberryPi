import unittest

import src.input

class TestCase(unittest.TestCase):
    def test_simon_says_test(self):
        device = src.input.init_devs('/dev/ttyACM0')
        self.assertEqual(str(src.input.request_value(device, 'x')), 'b\'Testx\'')
