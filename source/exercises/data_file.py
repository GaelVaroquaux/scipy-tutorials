"""Script to read in a column of numbers and calculate the min, max and sum.

Data is stored in data.txt.
"""

# Define the load_data function


if __name__ == '__main__':
    data = load_data('data.txt')
    # Python provides these basic math functions
    print('min: %f' % min(data))
    print('max: %f' % max(data))
    print('sum: %f' % sum(data))
