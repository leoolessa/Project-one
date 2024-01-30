import pandas as pd

def Junction(x):
    """_summary_
        the function searches for x in all values of the dictionary and returns the key associated with the first value that contains x. 
        If no value contains x, the function does not return anything.
    Args:
        x checks whether this value is present in any of the values of a dictionary

    Returns:
        If a match is found, the function returns the key associated with that value.
    """
    for key, value in dict_.items():
        if x in value:
            return key
