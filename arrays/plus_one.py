def plus_one(digits):
    '''
    start from the end of the list
    for each number
    if 9, change it to 0 and continue looping
    else, add one to the digit and stop looping
    '''
    is_carry = False
    for i in reversed(range(len(digits))):
        if digits[i] == 9:
            digits[i] = 0
            is_carry = True
        else:
            digits[i] = digits[i] + 1
            is_carry = False
            break
    if is_carry:
        digits = [1] + digits
    return digits

if __name__ == '__main__':
    digits = [9,9,9,9]
    res = plus_one(digits)
    print(f'\nres: {res}')

