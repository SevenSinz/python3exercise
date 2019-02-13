def sum_floats (nums):
    """ accept a list of nums. 
    - return sum of all floats
    - no floats: return 0 """
    
    return sum([num for num in nums if isinstance(num, float)])
    