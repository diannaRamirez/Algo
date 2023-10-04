import doctest
def decimal_to_negative_base_2(n):
    """
    This function returns the number negative base 2 of the decimal number of the input data.

    Args:
        int: The decimal number to convert.

    Returns:
        int: The negative base 2 number.

    Examples:
        >>> decimal_to_negative_base_2(0)
        0
        >>> decimal_to_negative_base_2(-19)
        111101
        >>> decimal_to_negative_base_2(4)
        100
        >>> decimal_to_negative_base_2(7)
        11011
    """
    if n == 0:
        return 0
    ans = ""
    while n != 0:
        rem = n % -2
        n = n // -2
        if rem < 0:
            rem += 2
            n += 1

        ans = str(rem) + ans

    return int(ans)

if __name__ == "__main__":
    doctest.testmod()
