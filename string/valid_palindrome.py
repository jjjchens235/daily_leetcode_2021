
def is_palindrome(s):
    import re
    pattern = re.compile(r'[^a-zA-Z1-9]')
    cleaned = re.sub(pattern, '', s).lower()
    return cleaned[::-1] == cleaned
    # conver the string using a)regex b) lower()
    # afterwards, compare cleaned string against it's reversed
