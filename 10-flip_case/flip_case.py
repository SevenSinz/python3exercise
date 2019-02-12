def flip_case(str, ltr):
    ltr = ltr.lower()
    swaped=''
    for char in str:
        if char.lower() == ltr:
            char = char.swapcase()
        swaped += char
    return swaped