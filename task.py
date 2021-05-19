
def conv_endian(num, endian='big'):
    """takes int and "type of" endian, converts int to hex and arranges according to endian. returns string"""
    if endian != 'big' and endian != 'little':
        return None

    negative = False
    if num < 0:
        negative = True
        num = abs(num)
    exp = 1
    before_conversion = []
    after_conversion = []
    hex_letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    # finds largest exponent of 16 that is less than the integer entered
    while 16 ** exp <= num:
        exp += 1
    exp -= 1

    # loops until 16^exp gets to 16^0
    while exp > 0:
        remain = num//16**exp                   # variable for the whole number(no decimal) created from num/16^exp
        before_conversion.append(remain)
        leftover = remain * 16**exp
        num = num - leftover                    # creates new number for variable remain calculation
        exp -= 1
    before_conversion.append(num)               # last number added to conversion list when exp = 0

    # converts digits over 9 to hex letters
    for num in before_conversion:
        if num > 9:
            after_conversion.append(hex_letters[num])
        else:
            after_conversion.append(num)

    length = (len(after_conversion))
    count_big = 0
    count_little = length - 1

    # formats return string. adds "0" to front of odd numbers and spacing every 2 characters
    if len(after_conversion) % 2 == 0:
        if endian == 'big':
            final_num = str(after_conversion[count_big]) + str(after_conversion[count_big + 1]) + " "
            count_big += 2
            while count_big < length:
                final_num = final_num + str(after_conversion[count_big]) + str(after_conversion[count_big + 1]) + " "
                count_big += 2
        else:  # for little endian
            final_num = str(after_conversion[count_little - 1]) + str(after_conversion[count_little]) + " "
            count_little -= 2
            while count_little > 0:
                final_num = final_num + str(after_conversion[count_little - 1]) + str(after_conversion[count_little])
                final_num = final_num + " "
                count_little -= 2
    else:
        if endian == 'big':
            final_num = "0" + str(after_conversion[count_big]) + " "
            count_big += 1
            while count_big < length-1:
                final_num = final_num + str(after_conversion[count_big]) + str(after_conversion[count_big + 1]) + " "
                count_big += 2
        else:  # for little endian
            final_num = ''
            while count_little > 0:
                final_num = final_num + str(after_conversion[count_little - 1]) + str(after_conversion[count_little]) + " "
                count_little -= 2
                if count_little == 0:
                    final_num = final_num + "0" + str(after_conversion[count_little])

    if negative is True:
        final_num = "-" + final_num

    return final_num
