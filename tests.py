import unittest
import random
import string
from task import conv_endian
from task import my_datetime
from task import conv_num


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

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

    def test1_function1(self):
        """Test for empty string"""
        msg = "Test failed for empty string"
        self.assertIsNone(conv_num(''), msg)

    def test2_function1(self):
        """Test for invalid integer"""
        num_str = "12345A"
        msg = "Test failed for " + num_str
        self.assertIsNone(conv_num(num_str), msg)

    def test3_function1(self):
        """Test for multiple decimal points in num_str"""
        num_str = "12.3.45"
        msg = "Test failed for " + num_str
        self.assertIsNone(conv_num(num_str), msg)

    def test4_function1(self):
        """Test for decimal 0"""
        num_str = "0"
        msg = "Test failed for " + num_str
        self.assertEqual(float(num_str), conv_num(num_str), msg)

    def test5_function1(self):
        """Test for valid integer"""
        num_str = "12345"
        msg = "Test failed for " + num_str
        self.assertEqual(float(num_str), conv_num(num_str), msg)

    def test6_function1(self):
        """Test for negative float"""
        num_str = "-123.45"
        msg = "Test failed for " + num_str
        self.assertEqual(float(num_str), conv_num(num_str), msg)

    def test7_function1(self):
        """Test for decimal point at the start of num_str"""
        num_str = ".45"
        msg = "Test failed for " + num_str
        self.assertEqual(float(num_str), conv_num(num_str), msg)

    def test8_function1(self):
        """Test for decimal point at the end of num_str"""
        num_str = "123."
        msg = "Test failed for " + num_str
        self.assertEqual(float(num_str), conv_num(num_str), msg)

    def test9_function1(self):
        """Test for invalid hexadecimal value"""
        num_str = "0xAZ4"
        msg = "Test failed for " + num_str
        self.assertIsNone(conv_num(num_str), msg)

    def test10_function1(self):
        """Test for valid hexadecimal value"""
        num_str = "0xAD4"
        msg = "Test failed for " + num_str
        self.assertEqual(int(num_str, 16), conv_num(num_str), msg)

    def test11_function1(self):
        """Test for negative hexadecimal value"""
        num_str = "-0xAD4"
        msg = "Test failed for " + num_str
        self.assertEqual(int(num_str, 16), conv_num(num_str), msg)

    def test12_function1(self):
        """Test for hexadecimal 0"""
        num_str = "0x0"
        msg = "Test failed for " + num_str
        self.assertEqual(int(num_str, 16), conv_num(num_str), msg)

    def test13_function1(self):
        """Randomly generate valid tests for conv_num"""
        num_tests = 5000
        for i in range(num_tests):
            num_str = ''
            # determine if negative value
            is_neg = random.randint(0, 1)
            if is_neg == 0:
                num_str += '-'
            # determine length to generate
            length = random.randint(1, 7)
            # determine if num_str is hexadecimal
            is_hex = random.randint(0, 1)
            # generate hex num_str
            if is_hex == 0:
                num_str += '0x'
                for j in range(length):
                    num_str += random.choice(string.hexdigits)
                msg = "Error on " + num_str + ": " + str(int(num_str, 16)) + " != " + str(conv_num(num_str))
                self.assertEqual(int(num_str, 16), conv_num(num_str), msg)
            # generate decimal num_str
            else:
                dec_loc = -1
                # determine location of decimal point
                if length > 1:
                    is_float = random.randint(0, 1)
                    if is_float == 0:
                        dec_loc = random.randint(0, length - 1)
                for j in range(length):
                    # add decimal point at appropriate location
                    if j == dec_loc:
                        num_str += '.'
                    else:
                        num_str += random.choice(string.digits)
                msg = "Error on " + num_str + ": " + str(float(num_str)) + " != " + str(conv_num(num_str))
                self.assertEqual(float(num_str), conv_num(num_str), msg)


if __name__ == '__main__':
    unittest.main()
