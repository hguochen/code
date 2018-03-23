
def check_digits(value):
    # 3(d_{1}+d_{4}+d_{7})+7(d_{2}+d_{5}+d_{8})+(d_{3}+d_{6}+d_{9})\mod 10=0.\,
    """
    Time: O(1)
    Space: O(1)
    """
    if len(value) != 9 or not int(value):
        return False
    first = 3 * (int(value[0]) + int(value[3]) + int(value[6]))
    second = 7 * (int(value[1]) + int(value[4]) + int(value[7]))
    third = int(value[2]) + int(value[5]) + int(value[8])
    result =  first + second + third
    return result % 10 == 0

if __name__ == '__main__':
    value1 = '111000025'
    value2 = '322271627'
    value3 = '322271626'
    print check_digits(value1) # True
    print check_digits(value2) # True
    print check_digits(value3) # True