def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    num1 = 0
    num2 = 0    
    index = 0
    result_list = [0] * len(line)
    for num in line:
        if num != 0:
            if num1 == 0:
                num1 = num
            elif num2 == 0:
                num2 = num
        if num1 != 0 and num2 != 0:            
            if num1 == num2:
                result_list[index] = num1 + num2                
                num1 = 0                
            else:
                result_list[index] = num1                
                num1 = num2
            num2 = 0
            index += 1
    if num1 != 0:
        result_list[index] = num1    
    return result_list