"""
Implement the quick sort algorithm.
"""

def qsort(lst):
    """ Quick sort: returns a sorted copy of the list.
    """
    # Implement the quick sort logic here
    return lst

# And now check that qsort does sort:
assert qsort(range(10)) == range(10)
assert qsort(range(10)[::-1]) == range(10)
assert qsort([1, 4, 2, 5, 3]) == sorted([1, 4, 2, 5, 3])


