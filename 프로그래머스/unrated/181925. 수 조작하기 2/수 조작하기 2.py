def solution(numLog):
    result = ''
    for i in range(len(numLog)-1):
        n = numLog[i] - numLog[i+1]
        if n == -1:
            result += 'w'
        elif n == 1:
            result += 's'
        elif n == -10:
            result += 'd'
        else:
            result += 'a'
    return result