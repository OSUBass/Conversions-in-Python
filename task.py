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