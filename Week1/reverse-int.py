def reverse(x):
    if x == 0:
        return 0
    
    negative = False
    str_x = str(x)
    if str_x[0] == "-":
        negative = True
        str_x = str_x[1:]
    rever = str_x[::-1]
    check_zero = 0
    counter = 0
    while rever[counter] == "0":
        check_zero += 1
        counter += 1
    final = rever[check_zero::]
    if negative == True:
        fin_negative = 0 - int(final)
        if  fin_negative < -2147483648:
            return 0
        return fin_negative
    if int(final) > 2147483647:
        return 0
    return int(rever)


print(reverse(-89))