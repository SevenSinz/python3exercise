def multiply_even_numbers(nums):
    """accepts a list of numbers and returns the product of all even numbers 
    in the list. 
    If there are no even numbers, the function should return 1."""
    multi = 1

    for num in nums:
        if num % 2 == 0:
            multi = multi * num

    return multi