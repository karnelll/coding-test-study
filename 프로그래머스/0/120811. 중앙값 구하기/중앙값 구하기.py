def solution(array):
    n = len(array)
    
    array.sort()
    
    if n % 2 == 0:  
        answer = array[n // 2 - 1] 
    else:  
        answer = array[n // 2]  
        
    return answer
