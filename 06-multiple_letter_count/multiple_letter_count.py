def multiple_letter_count(str):
    """" count frequency """
    counter = {}

    for ltr in str:
        counter[ltr] = counter.get(ltr, 0) + 1
    
    return counter
