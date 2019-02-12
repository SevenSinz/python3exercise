def is_palindrome(string):
    '''is a palindrome?'''
    string = string.strip()
    string = string.lower()

    return string == string[::-1]
