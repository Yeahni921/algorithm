def solution(arr):
    idx = []
    if 2 not in arr:
        return [-1]
    for i in range(len(arr)):
        if arr[i] == 2:
            idx.append(i)
    return arr[idx[0]:idx[-1]+1]