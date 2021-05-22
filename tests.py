import unittest
from task import conv_endian
from task import my_datetime
import random


class TestCase(unittest.TestCase):

    def test1_function2(self):
        expected = '01-01-1970'
        self.assertEqual(expected, my_datetime(0))

    def test2_function2(self):
        expected = '02-01-1970'
        self.assertEqual(expected, my_datetime(2721600))

    def test3_function2(self):
        expected = '01-01-1971'
        self.assertEqual(expected, my_datetime(31536000))

    def test4_function2(self):
        expected = '02-29-1972'
        self.assertEqual(expected, my_datetime(68212800))

    def test5_function2(self):
        expected = '03-01-1972'
        self.assertEqual(expected, my_datetime(68256000))

    def test6_function2(self):
        expected = '11-29-1973'
        self.assertEqual(expected, my_datetime(123456789))

    def test8_function2(self):
        expected = '03-01-2100'
        self.assertEqual(expected, my_datetime(4107542400))

    def test9_function2(self):
        expected = '12-22-2282'
        self.assertEqual(expected, my_datetime(9876543210))

    def test10_function2(self):
        expected = '02-29-8360'
        self.assertEqual(expected, my_datetime(201653971200))

    def test1(self):
        self.assertTrue(True)

    def test2_function3(self):
        """tests for correct conversion of decimal to hex in both negative and positive random decimal numbers
        for big endian"""
        num_tests = 1000
        for i in range(num_tests):
            negative = False
            num = random.randint(-9223372036854775807, 9223372036854775807)

            # changes negative values to positive for conversion and sets flag for negative value
            if num < 0:
                negative = True
                num = abs(num)
            correct_hex = str(hex(num))         # converts decimal to string hex with built-in
            correct_hex = correct_hex[2:]      # takes off the "0x" from front of hex

            # formats hex str: adds spacing to hex (every 2 chars) & adds 0 to front if length is odd.
            if len(correct_hex) % 2 != 0:
                space = 1
                format_hex = '0'
            else:
                space = 0
                format_hex = ''
            for char in correct_hex:
                format_hex = format_hex + char
                space += 1
                if space == 2:
                    format_hex = format_hex + ' '
                    space = 0
            format_hex = format_hex[:-1]

            # converts back to negative value if negative variable is True
            if negative is True:
                format_hex = '-' + format_hex
            if negative is True:
                num = num * -1

            my_hex = conv_endian(num, endian='big')
            message = "test failed for num " + str(num)
            self.assertEqual(format_hex.upper(), my_hex, message)


if __name__ == '__main__':
    unittest.main()
