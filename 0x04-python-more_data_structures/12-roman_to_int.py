#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    r_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    my_list_keys = list(r_n.keys())
    x = 0
    y = 0
    z = [0]
    for i in roman_string:
        for j in my_list_keys:
            if j == i:
                if r_n.get(i) <= y:
                    x += remove_list(z)
                    z = [r_n.get(i)]
                else:
                    z.append(r_n.get(i))
                y = r_n.get(i)
    x += remove_list(z)
    return (x)


def remove_list(z):
    remove_string = 0
    big_list = max(z)

    for num in z:
        if big_list > num:
            remove_string += num
    return (big_list - remove_string)
