"""
String Calculator Module
------------------------
@author: [student's name] - [student's email]
@date: [date of creation]
@description: This module is part of an Applied Software Engineering exercise at CMU-Q. It includes
              a string calculator that interprets a string input and calculates the result based on
              the rules defined. This exercise is intended to practice TDD (Test-Driven Development)
              and learn how to handle various string parsing challenges in Python.

Purpose:
--------
The string calculator should:
1. Handle an input string that contains numbers separated by commas.
2. Return the sum of these numbers as a string.
3. Be extended through various iterations to handle newlines as separators, custom delimiters,
   negative number validation, and more complex error handling.

Usage:
------
This module should be used in conjunction with a testing framework to develop each feature
incrementally using TDD practices. Students are expected to write tests before implementing
or modifying the functionality in `add`.

Example:
--------
    >>> from calculator import add
    >>> add("1,2")
    '3'
    >>> add("//;\\n1;2")
    '3'
"""
def add(s: str) -> str:
    """
    Adds numbers in a given string.

    This function takes a single string input that can contain numbers separated by commas
    and potentially other specified delimiters. It returns the sum of these numbers as a string.
    Initial versions will handle basic input, with subsequent iterations to introduce handling of
    different delimiters, newlines, and error conditions.

    Parameters:
    - s (str): A string containing the numbers to add.

    Returns:
    - str: The sum of the numbers as a string.

    Raises:
    - ValueError: If the input string is malformed or contains invalid characters or formats.

    Example:
    --------
        >>> add("1,2")
        '3'
        >>> add("1,2,3")
        '6'
        >>>
    """
    
    if s.endswith(","):
        return "Number expected but EOF found."
    if ",\n" in s:
        return f"Number expected but '\\n' found at position {s.find(',\n')}."
    s = s.replace("\n", ",")
    numbers = s.split(",")
    sum = 0
    negatives = []
    for num in numbers:
        if num == "":
            return "Number expected but ',' found."
        if float(num) < 0:
            negatives.append(num)
        elif "." in num:
            sum += float(num)
        else:
            sum += int(num)
    if negatives:   # if negatives is not empty
        return f"Negative not allowed : {', '.join(negatives)}"
    return str(sum)
    
