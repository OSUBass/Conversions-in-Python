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

    def test1_function3(self):
        """tests for correct conversion of decimal to hex in both negative
        & positive random integers for big endian"""
        num_tests = 50000
        for i in range(num_tests):
            negative = False
            num = random.randint(-9223372036854775, 9223372036854775807)

            # changes negative values to positive for conversion & sets flag for negative
            if num < 0:
                negative = True
                num = abs(num)

            # converts integer to hex string & removes "0x" from front
            hex_string = (str(hex(num)))[2:]

            if len(hex_string) % 2 != 0:
                hex_string = '0' + hex_string

            # add space to hex string every 2 characters
            big_hex = ''
            for x in range(0, len(hex_string), 2):
                big_hex = big_hex + hex_string[x:x+2] + " "
            big_hex = big_hex[:-1]

            # converts back to negative value if negative variable is True
            if negative is True:
                big_hex = '-' + big_hex
                num = num * -1

            my_big_hex = conv_endian(num, endian='big')
            big_message = "big endian test failed for num " + str(num)
            self.assertEqual(big_hex.upper(), my_big_hex, big_message)

    def test2_function3(self):
        """tests for correct conversion of decimal to hex in both negative &
        positive random integers for little endian"""
        num_tests = 50000
        for i in range(num_tests):
            negative = False
            num = random.randint(-9223372036854775807, 9223372036854775807)

            # changes negative values to positive for conversion & sets flag for negative
            if num < 0:
                negative = True
                num = abs(num)

            # converts integer to hex string & removes "0x" from front
            hex_string = (str(hex(num)))[2:]

            if len(hex_string) % 2 != 0:
                hex_string = '0' + hex_string

            # change byte order of hex into little endian
            little_hex = ''
            count = len(hex_string)-1
            while count > 0:
                little_hex = little_hex + hex_string[count - 1] + hex_string[count] + " "
                count -= 2
            little_hex = little_hex[:-1]

            # converts back to negative value if negative variable is True
            if negative is True:
                little_hex = '-' + little_hex
                num = num * -1

            my_little_hex = conv_endian(num, endian='little')
            little_message = "little endian test failed for num " + str(num)
            self.assertEqual(little_hex.upper(), my_little_hex, little_message)

    def test3_function3(self):
        """tests for return of None if invalid endian is entered"""
        expected = None
        num = random.randint(-9223372036854775807, 9223372036854775807)
        message = "return None test failed for num " + str(num)
        self.assertEqual(conv_endian(num, endian='small'), expected, message)

    def test4_function3(self):
        """tests for return of 00 if number 0 is entered into function"""
        expected = '00'
        message = "return 00 test failed for 0"
        self.assertEqual(conv_endian(0), expected, message)

    def test5_function3(self):
        """tests for correct return of single digit integers"""
        expected = '09'
        message = "return test failed for single digit"
        self.assertEqual(conv_endian(9), expected, message)

    def test6_function3(self):
        """tests for return of correct return of single digit integers for 'little' endian"""
        expected = '05'
        message = "return test failed for single digit little endian"
        self.assertEqual(conv_endian(5, 'little'), expected, message)

    def test7_function3(self):
        """tests for return of example given in assignment requirements"""
        expected = '0E 91 A2'
        message = "return 0E 91 A2 test failed for 954786"
        self.assertEqual(conv_endian(954786, 'big'), expected, message)

    def test8_function3(self):
        """tests for return of example given in assignment requirements"""
        expected = '-A2 91 0E'
        message = "return -A2 91 0E test failed for -954786 little endian"
        self.assertEqual(conv_endian(-954786, 'little'), expected, message)

    def test9_function3(self):
        """tests for return of very large integer"""
        expected = '7F FF FF FF FF FF FF FF'
        message = "return test failed for 9223372036854775807"
        self.assertEqual(conv_endian(9223372036854775807, 'big'), expected, message)

    def test10_function3(self):
        """tests for return of very large integer & little endian"""
        expected = 'FF FF FF FF FF FF FF 7F'
        message = "test failed for little endian 9223372036854775807"
        self.assertEqual(conv_endian(9223372036854775807, 'little'), expected, message)

    def test11_function3(self):
        """tests for return of very large negative integer"""
        expected = '-8A C7 23 04 89 E7 FF FF'
        message = "test failed for -9999999999999999999"
        self.assertEqual(conv_endian(-9999999999999999999), expected, message)

    def test12_function3(self):
        """test for very large negative integer & little endian"""
        expected = '-FF FF E7 89 04 23 C7 8A'
        message = "test failed for -9999999999999999999"
        self.assertEqual(conv_endian(-9999999999999999999, 'little'), expected, message)

    def test13_function3(self):
        """tests for return of mid-range integer"""
        expected = '0A D4'
        message = "return 0A D4 test failed for 2772"
        self.assertEqual(conv_endian(2772), expected, message)

    def test14_function3(self):
        """tests for return of negative mid-range integer in little endian"""
        expected = '-D4 0A'
        message = "return -D4 0A test failed for -2772"
        self.assertEqual(conv_endian(-2772, endian='little'), expected, message)

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
