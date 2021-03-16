"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print each item in the list.

    For example:

    >>> output_all_items([1, 'hello', True])
    1
    hello
    True
    """

    for item in items:
        print(item)

def get_all_evens(nums):
    """Given a list of integers, return all that are even numbers.

    For example:

    >>> get_all_evens([7, 8, 10, 1, 2, 2])
    [8, 10, 2, 2]
    """

    evenNums = []
    for num in nums:
        if num % 2 == 0:
            evenNums.append(num)
    return evenNums

###### COME BACK

def get_odd_indices(items):
    """Get all odd indices from a list.

    For example:

    >>> get_odd_indices([1, 'hello', True, 500])
    ['hello', 500]
    """

    result = []

    for index in items:
        if index % 2 != 0:
            result.append(items[index])
    return result


def print_as_numbered_list(items):
    """Given an list, output a numbered list

    For example:

    >>> print_as_numbered_list([1, 'hello', True])
    1. 1
    2. hello
    3. True
    """

    count = 1
    for i in items:
        print(f"{count}. {i}")
        count += 1


def get_range(start, stop):
    """Return a list of numbers in a certain range.

    For example:

    >>> get_range(0, 5)
    [0, 1, 2, 3, 4]

    >>> get_range(1, 3)
    [1, 2]
    """

    nums = []
    num = start
    for num in range(start, stop):
        if num < stop:
            nums.append(num)
            num +=1
    return nums


def censor_vowels(word):
    pass  # TODO: replace this line with your code


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code