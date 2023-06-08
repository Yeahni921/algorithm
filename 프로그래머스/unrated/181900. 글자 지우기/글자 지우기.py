def solution(my_string, indices):
    chars = list(my_string)  # Convert string to a list of characters

    # Remove characters at the specified indices
    for idx in sorted(indices, reverse=True):
        del chars[idx]

    return ''.join(chars)