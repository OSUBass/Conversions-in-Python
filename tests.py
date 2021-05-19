import unittest
from task import conv_endian
import random


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def test2_function3(self):
        """tests for correct conversion of decimal to hex in both negative and positive random decimal numbers
        for big endian"""
        num_tests = 100
        for i in range(num_tests):
            negative = False
            num = random.randint(-999999999, 999999999)

            # changes negative values to positive for conversion and sets flag for negative value
            if num < 0:
                negative = True
                num = abs(num)
            correct_hex = str(hex(num))         # converts decimal to string hex with built-in
            correct_hex = correct_hex[2:]       # takes off the "0x" from front of hex

            # formats hex: adds spacing to hex (every 2 chars) & adds 0 to front if length is odd.
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
