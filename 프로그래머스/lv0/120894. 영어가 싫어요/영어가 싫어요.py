def solution(numbers):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for idx, val in enumerate(nums):
        numbers = numbers.replace(val, str(idx))
        
    return int(numbers)
    