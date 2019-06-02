

num_in = input('Enter an integer: ')


roman_num_ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
roman_num_tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
roman_num_hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
roman_num_thousands = ['', 'M', 'MM', 'MMM']

try:
    if int(num_in) < 1 or int(num_in) > 3999:
        print('Input must be between 1 and 3999')

    elif len(str(num_in)) == 4:
        print('In Roman numerals,', num_in, 'is', roman_num_thousands[int(str(num_in)[0])] +
              roman_num_hundreds[int(str(num_in)[1])] + roman_num_tens[int(str(num_in)[2])] +
              roman_num_ones[int(str(num_in)[3])])

    elif len(str(num_in)) == 3:
        print('In Roman numerals,', num_in, 'is', roman_num_hundreds[int(str(num_in)[0])] +
              roman_num_tens[int(str(num_in)[1])] + roman_num_ones[int(str(num_in)[2])])

    elif len(str(num_in)) == 2:
        print('In Roman numerals,', num_in, 'is', roman_num_tens[int(str(num_in)[0])] +
              roman_num_ones[int(str(num_in)[1])])

    elif len(str(num_in)) == 1:
        print('In Roman numerals,', num_in, 'is', roman_num_ones[int(num_in)])

except:
    print("Please Enter Integers!!!")
