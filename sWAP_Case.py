def swap_case(s):
    swapped=""

    for c in s:
        if c.islower():
            swapped=swapped+c.upper()
        elif c.upper():
            swapped=swapped+c.lower()
        else:
            swapped=swapped+c

    return swapped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
