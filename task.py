
def my_datetime(num_sec):
    """takes an integer value that represents the number of seconds since
    January 1st 1970 and returns date string with the format MM-DD-YYYY"""

    year = 1970
    month = 1
    day = 1
    leap = False

    # maximum days per month in non leap year
    days_max = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }

    # 86,400 seconds per day, while days remain to be added
    while num_sec >= 86400:

        # if it's the end of the year, increment the year and check for leap
        if month == 12 and day == 31:
            year += 1
            month = 1
            day = 1

            # if year is evenly divisible by 4 but not 100
            # or if year is divisible by 400, then leap year
            if year % 4 == 0 and year % 100 != 0:
                leap = True
            elif year % 400 == 0:
                leap = True

            num_sec -= 86400

        # if it's the end of another month, increment the month
        elif day >= days_max[month]:

            # special case runs once on leap year moving from 2/28 to 2/29
            if month == 2 and leap is True:
                day += 1
                leap = False
                num_sec -= 86400

            # otherwise increment to the next month and reset day
            else:
                month += 1
                day = 1
                num_sec -= 86400

        # otherwise simply increment day
        else:
            day += 1
            num_sec -= 86400

    # add leading zero for single digit days and months
    if day < 10:
        day = '0' + str(day)
    if month < 10:
        month = '0' + str(month)

    # return date string in MM-DD-YYYY format
    return str(month) + '-' + str(day) + '-' + str(year)


def format_hex(conv, endian):
    """takes hex_conversion list and endian type. Turns list into a string with
    spacing every 2 characters in big or little endian order. returns formatted string"""
    final = ''
    big = 0
    little = (len(conv)) - 1
    if endian == 'big':
        while big < (len(conv)):
            final = final + str(conv[big]) + str(conv[big + 1]) + " "
            big += 2
    else:
        while little > 0:
            final = final + str(conv[little - 1]) + str(conv[little]) + " "
            little -= 2
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
        remain = num//16**exp         # whole number(no decimal) of remainder saved
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
