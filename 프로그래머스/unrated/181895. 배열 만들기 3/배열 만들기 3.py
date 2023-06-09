def solution(arr, intervals):
    result = []
    for interval in intervals:
        a, b = interval
        result.append(arr[a:b+1])
    return result[0] +result[1]