def main(first,last):
    """
    Given two strings, first_name and last_name, return a single string in the format "last, first".
    Args:
        first: str
        last: str
    Returns:
        str: return answer.
    """
    return  first+", "+last
first=input()
last=input()
print(main(first,last))