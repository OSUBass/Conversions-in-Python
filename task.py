import string


def my_datetime(num_sec):
    """takes an integer value that represents the number of seconds since
    January 1st 1970 and returns date string with the format MM-DD-YYYY"""

    year = 1970
    month = 1
    day = 1
    days_per_year = 365
    days_per_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }

    # 86,400 seconds per day, while days remain to be incremented
    while num_sec >= 86400:

        # if a full year can be incremented
        if num_sec >= days_per_year * 86400:
            num_sec -= days_per_year * 86400
            year += 1

            # if year is evenly divisible by 4 but not 100
            # or if year is divisible by 400, then leap year
            if year % 4 == 0 and year % 100 != 0:
                days_per_year = 366
                days_per_month[2] = 29
            elif year % 400 == 0:
                days_per_year = 366
                days_per_month[2] = 29
            else:
                days_per_year = 365
                days_per_month[2] = 28

        # if a full month can be incremented
        elif num_sec >= days_per_month[month] * 86400:
            num_sec -= days_per_month[month] * 86400
            month += 1

        # otherwise simply increment day
        else:
            num_sec -= 86400
            day += 1

    return str(month).zfill(2) + '-' + str(day).zfill(2) + '-' + str(year)


def conv_hex(num_str, neg_flag):
    """takes num_str, converts it to an integer as if its a hexadecimal
    number, returns num_int"""
    hex_values = {'A': 10, 'a': 10, 'B': 11, 'b': 11, 'C': 12, 'c': 12,
                  'D': 13, 'd': 13, 'E': 14, 'e': 14, 'F': 15, 'f': 15}
    num_int = 0
    for i in range(0, len(num_str)):
        # return None if any invalid characters are found
        if num_str[i] not in string.hexdigits:
            return None

        # num_int = num_int + (value of digit) * 16^(place number - 1)
        # for 0-9
        if num_str[i] in string.digits:
            num_int += (ord(num_str[i]) - 48) * 16 ** (len(num_str) - i - 1)
        # for A-F and a-f
        else:
            num_int += (hex_values[num_str[i]]) * 16 ** (len(num_str) - i - 1)

    # convert back to string
    if neg_flag is True and num_int != 0:
        num_final = "-"
    else:
        num_final = ""

    n = 0
    # find highest place
    while num_int / (10 ** n) >= 1:
        n += 1
    if n > 0:
        n -= 1
    # calculate digits
    while n >= 1:
        digit = num_int // (10 ** n)
        num_final += string.digits[digit]
        num_int -= digit * (10 ** n)
        n -= 1
    # add final digit
    num_final += string.digits[num_int]
    return num_final


def conv_dec(num_str, neg_flag):
    """takes num_str, converts it to a base 10 number as if its a floating
    point number, returns num"""
    if not num_str:
        return None

    # find decimal location in num_str
    dec_point = num_str.find('.')
    # if no decimal point
    if dec_point == -1:
        dec_point = len(num_str)
    # if decimal point is at the end of the string
    elif dec_point == len(num_str) - 1:
        num_str = num_str[:dec_point]
    # all other decimal point locations
    else:
        num_str = num_str[:dec_point] + num_str[dec_point + 1:]

    num = 0
    for i in range(0, len(num_str)):
        # return None if any invalid characters are found
        if num_str[i] not in string.digits:
            return None

        # num = num + (ASCII code of digit - ASCII code for 0) * 10^(distance
        # from decimal - 1)
        num += (ord(num_str[i]) - 48) * 10 ** (dec_point - i - 1)

    # rounds float values to the appropriate decimal place
    num = round(num, len(num_str) - dec_point)
    if neg_flag is True:
        num = 0 - num

    return num


def conv_num(num_str):
    """takes num_str, converts it to a base 10 number, returns num"""

    # check for empty string
    if not num_str:
        return None

    # check for negative value
    neg_flag = False
    if num_str[0] == '-':
        neg_flag = True
        num_str = num_str[1:]

    # check if hexadecimal number
    if num_str[:2] == "0x":
        num = conv_hex(num_str[2:], neg_flag)
    else:
        num = conv_dec(num_str, neg_flag)

    return num


def format_hex(conv, endian):
    """takes hex_conversion list and endian type. Turns list into a string with
    spacing every 2 characters in big or little endian order. returns formatted string"""
    final = ''
    if endian == 'big':
        count = 0
        while count < (len(conv)):
            final = final + str(conv[count]) + str(conv[count + 1]) + " "
            count += 2
    else:
        count = (len(conv)) - 1
        while count > 0:
            final = final + str(conv[count - 1]) + str(conv[count]) + " "
            count -= 2
    final = final[:-1]
    return final


def conv_endian(num, endian='big'):
    """takes int and "type of" endian, converts int to hex and arranges according to endian. returns string"""
    if endian != 'big' and endian != 'little':
        return None

    negative = False
    if num < 0:
        negative = True
        num = abs(num)

    # finds largest exponent of 16 that is less than the number entered
    exp = 1
    while 16**exp <= num:
        exp += 1
    exp -= 1

    # loops until 16^exp gets to 16^0 and calculates conversion. Adds each remainder digit to hex_conv list.
    hex_conv = []
    while exp > 0:
        remain = num // 16**exp         # whole number(no decimal) of remainder saved
        hex_conv.append(remain)
        num = num - (remain * 16**exp)           # creates new number for variable remain calculation
        exp -= 1
    hex_conv.append(num)               # last number added to conversion list when exp = 0

    # converts digits over 9 to hex letters
    hex_letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hex_conv = [x if x < 10 else hex_letters[x] for x in hex_conv]

    if len(hex_conv) % 2 != 0:
        hex_conv.insert(0, '0')
    final = format_hex(hex_conv, endian)

    if negative is True:
        final = "-" + final

    return final
