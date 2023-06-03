def solution(n):
    result = [n]
    
    for i in result:
        if i == 1:
            break
            
        if i % 2 == 0:
            result.append(i/2)
        else:
            result.append(3 * i +1)
        
    return result