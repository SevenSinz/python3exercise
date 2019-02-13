def mode(lst):
    """ 1- create the frequency counter dictionary. 
    2- Find the max amoung values
    3- loop over dictionary with key: value and if key equals the max, 
        return the value """
        
    counter = {}

    for val in lst:
        counter[val] = counter.get(val, 0) + 1
    
    max_count = max(counter.values())

    for (digit, freq) in counter.items():
        if freq == max_count:
            return digit

