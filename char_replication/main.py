

def transformation(cad: str) -> str:
    """
    Transforms a string by repeating characters based on following digit values.

    Iterates through the input string and when a non-zero digit is found, repeats 
    the previous character that many times and appends it to the result.

    Args:
        cad (str): The input string containing characters and digits.

    Returns:
        str: The transformed string with characters repeated according to 
             subsequent digit values.

    Example:
        >>> transf
    ormation("a3b2c1")
        'aaabbc'

    Note:
        - Only processes non-zero digits
        - Uses the character immediately before each digit for repetition
        - Non-digit characters are skipped unless referenced by a following digit
    """
    result = ""
    for c in cad:
        if c.isdigit():
            c1 = int(c)
            if c1 != 0:
                letter = cad[cad.index(c) - 1]    
            result = result + letter * c1
    return result


def main():
    string_input = input("Enter a string: ")
    transformed_string = transformation(string_input)
    print("Transformed string:", transformed_string)


if __name__ == "__main__":
    main()
