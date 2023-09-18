def solution(n_str):
    n = len(n_str)
    for i in range(n):
        if n_str[i] != '0':
            return n_str[i:]
    return n_str
    