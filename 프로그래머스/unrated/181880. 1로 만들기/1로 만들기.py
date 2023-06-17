def solution(num_list):
    count = 0
    for i in num_list:
        while i >= 2:
            while i % 2 != 0:
                i -= 1
            i = i//2
            count += 1
    return count