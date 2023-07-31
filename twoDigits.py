for numberOne in range(1, 100):
    tens_digit = numberOne // 10
    ones_digit = numberOne % 10
    
    if tens_digit != ones_digit:
        reverse_number = ones_digit * 10 + tens_digit
        if reverse_number > numberOne:
            print("{:02}".format(numberOne), end=" , ")

