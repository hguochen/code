"""
https://practice.geeksforgeeks.org/problems/generate-ip-addresses/1

Given a string s containing only digits, Your task is to complete the function genIp which
returns a vector containing all possible combination of valid IPv4 ip address and takes only
a string s as its only argument .
"""

def generate_ip_address(string):
    """
    Time: O(2^n)
    Space: O(2^n)
    """
    if not string:
        return []
    result = []
    generate_ip_address_util(string, 3, "", result)
    return result

def generate_ip_address_util(string, dots, prefix, result):
    if len(string) < 1:
        if dots == 0 and prefix[-1] != ".":
            result.append(prefix)
        return
    elif dots == 0:
        if int(string) <= 255:
            if (int(string) > 0 and string[0] == "0") or (int(string) == 0 and len(string) > 1):
                return
            result.append(prefix + string)
        return
    if string[0] == "0":
        generate_ip_address_util(string[1:], dots-1, prefix + "0.", result)
        return
    for i in xrange(1, 4):
        temp = string[:i]
        rem = string[i:]
        if len(temp) > 0 and int(temp) > 255 or (int(temp) != 0 and temp[0] == "0"):
            continue
        new_prefix = prefix + temp
        if dots > 0:
            new_prefix += "."
        generate_ip_address_util(rem, dots-1, new_prefix, result)


if __name__ == '__main__':
    str1 = "11211"
    str2 = "25525511135"
    str3 = "0000"
    str4 = "010010"
    print generate_ip_address(str1)
    print generate_ip_address(str2)
    print generate_ip_address(str3)
    print generate_ip_address(str4)
