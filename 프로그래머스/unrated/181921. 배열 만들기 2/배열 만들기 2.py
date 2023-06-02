def solution(l, r):
    result = []
    
    for num in range(l, r+1):
        if all(digit in ["0", "5"] for digit in str(num)):
            result.append(num)
            
    if len(result) == 0:
        return [-1]
    else:
        return result
        
        
        
