def subsets(nums):
    result = [[]]
        
    for num in nums:
        for i in range(len(result)):
            result.append(result[i] + [num])
    return result
            
print(subsets([1,2,3]))