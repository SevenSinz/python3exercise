def compact(lst):
    """return a list of truthy values in input list"""
    return [val for val in lst if bool(val) == True]