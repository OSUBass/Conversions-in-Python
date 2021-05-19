def format_even_hex(big, little, conv, endian):
    """takes big_counter, little_counter, hex_conversion list and endian.
    formats return string for even numbers with spacing every 2 characters"""
    final = ''
    length = (len(conv))
    if endian == 'big':
        while big < length:
            final = final + str(conv[big]) + str(conv[big + 1]) + " "
            big += 2
    else:  # for little endian
        while little > 0:
            final = final + str(conv[little - 1]) + str(conv[little]) + " "
            little -= 2
    return final


def format_odd_hex(big, little, conv, endian):
    """takes big_counter, little_counter, hex_conversion list and endian.
        formats return string for odd numbers by adding "0" to front and spacing every 2 characters"""
    final = ''
    length = (len(conv))
    if endian == 'big':
        final = "0" + str(conv[big]) + " "
        big += 1
        while big < length - 1:
            final = final + str(conv[big]) + str(conv[big + 1]) + " "
            big += 2
    else:
        while little > 0:
            final = final + str(conv[little - 1]) + str(conv[little]) + " "
            little -= 2
            if little == 0:
                final = final + "0" + str(conv[little])
    return final


def conv_endian(num, endian='big'):
    """takes int and "type of" endian, converts int to hex and arranges according to endian. returns string"""
    if endian != 'big' and endian != 'little':
        return None

    negative = False
    if num < 0:
        negative = True
        num = abs(num)

    # finds largest exponent of 16 that is less than the integer entered
    exp = 1
    while 16 ** exp <= num:
        exp += 1
    exp -= 1

    # loops until 16^exp gets to 16^0
    hex_conv = []
    while exp > 0:
        remain = num//16**exp         # variable for the whole number(no decimal) created from num/16^exp
        hex_conv.append(remain)
        leftover = remain * 16**exp
        num = num - leftover            # creates new number for variable remain calculation
        exp -= 1
    hex_conv.append(num)               # last number added to conversion list when exp = 0

    # converts digits over 9 to hex letters
    hex_letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hex_conv = [x if x < 10 else hex_letters[x] for x in hex_conv]

    count_big = 0
    count_little = (len(hex_conv)) - 1
    if len(hex_conv) % 2 == 0:
        final = format_even_hex(count_big, count_little, hex_conv, endian)
    else:
        final = format_odd_hex(count_big, count_little, hex_conv, endian)

    if negative is True:
        final = "-" + final

    return final
