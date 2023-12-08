
            
            
            
def maxSubArray(nums):
    maximum=-float('inf')
    total=0
    for i in range(len(nums)):
        total+=nums[i]
        if nums[i] > total:
            total = nums[i]
        if total > maximum:
            maximum = total
    return maximum
            
        
        
            

input = [-1, 3, 4, -2, 1]
answer = 7

output = maxSubArray(input)
print(output)
print(answer)

