#!/usr/bin/python3
def remove_char_at(str, n):
    """
    Parameters
    ----------
    str : str
        The string from which the position needs to be removed
    n : int
        The position of the string to be deleted

    Deletes the character at the nth position of the str.
    The function:
    1. copies the string.
    2. deletes a position of the passed string.
    3. returns the string without a deleted position

    Returns
    -------
    str
        The copy of the string without the deleted position
    """

    new_str = ""

    for i in range(len(str)):
        if i != n:
            new_str += str[i]

    return new_str
