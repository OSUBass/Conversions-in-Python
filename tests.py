import unittest
from task import conv_endian
import random


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)


    def function3_spacing(self, hex_string):
        space = 0
        format_hex = ''
        for char in hex_string:
            format_hex = format_hex + char
            space += 1
            if space == 2:
                format_hex = format_hex + ' '
                space = 0
        format_hex = format_hex[:-1]
        return format_hex


    def test2_function3(self):
        """tests for correct conversion of decimal to hex in both negative and positive random decimal numbers
        for big endian"""
        num_tests = 1000
        test_case = 0
        for i in range(num_tests):
            negative = False
            num = random.randint(-9223372036854775807, 9223372036854775807)

            # changes negative values to positive for conversion and sets flag for negative value
            if num < 0:
                negative = True
                num = abs(num)

            correct_hex = str(hex(num))         # converts decimal to string hex with built-in
            correct_hex = correct_hex[2:]      # takes off the "0x" from front of hex

            if len(correct_hex) % 2 != 0:
                correct_hex = '0' + correct_hex

            big_hex = self.function3_spacing(correct_hex)

            little_hex = ''
            count = len(correct_hex)-1
            for char in correct_hex:
                while count > 0:
                    little_hex = little_hex + correct_hex[count - 1] + correct_hex[count]
                    count -= 2
            little_hex = self.function3_spacing(little_hex)

            # converts back to negative value if negative variable is True
            if negative is True:
                big_hex = '-' + big_hex
                little_hex = '-' + little_hex
            if negative is True:
                num = num * -1

            my_big_hex = conv_endian(num, endian='big')
            my_little_hex = conv_endian(num, endian = 'little')
            big_message = "big endian test failed for num " + str(num)
            little_message = "little endian test failed for num " + str(num)
            if test_case == 0:
                print("big hex:")
                print(my_big_hex)
                print(big_hex.upper())
                print(little_hex.upper())
                self.assertEqual(big_hex.upper(), my_big_hex, big_message)
                test_case += 1
            else:
                print("little hex:")
                print(my_little_hex)
                print(little_hex.upper())
                print(big_hex.upper())
                self.assertEqual(little_hex.upper(), my_little_hex, little_message)
                test_case -= 1


if __name__ == '__main__':
    unittest.main()
