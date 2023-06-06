def solution(my_string, is_suffix):
    word = []
    for i in range(len(my_string)):
        word.append(my_string[i:])
    if is_suffix in word:
        return 1
    else:
        return 0