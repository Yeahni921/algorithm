def solution(a, b):
    n = str(a)+str(b)
    m = str(b)+str(a)
    
    return max(int(n), int(m))