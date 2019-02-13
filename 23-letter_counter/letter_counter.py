def letter_counter(phrase):
    """ accept a string and returns a function. 
    - inner function: accept a letter: return frequency of the letter in string
    - case insensitive.
    >>> py
    >>> counter = letter_counter('Amazing')

    >>> counter('a') # 2
    >>> counter('m') # 1

    >>> counter2 = letter_counter('This Is Really Fun!')

    >>> counter2('i') # 2
    >>> counter2('t') # 1

    """
    phrase = phrase.lower()

    def inner(ltr):
        return phrase.count(ltr.lower())

    return inner