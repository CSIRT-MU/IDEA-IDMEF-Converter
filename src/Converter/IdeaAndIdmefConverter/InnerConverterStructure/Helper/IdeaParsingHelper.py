
def correct_braces(string):
    """
    Check if string has correct braces "{" and "}"

    :param string: String with braces to be chekced
    :return: true if braces are correct, otherwise false
    """

    if string is None:
        raise ValueError("String to check correct braces was None")
    braces_count = 0
    quotation = False
    for character in string:
        if character == '{' and not quotation:
            braces_count += 1
        if character == '}' and not quotation:
            braces_count -= 1
        if character == '"':
            quotation = not quotation
        if braces_count < 0:
            return False
    return braces_count == 0
