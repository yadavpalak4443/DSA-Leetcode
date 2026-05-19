#Move all zeros in the array to the end while maintaining the relative order of the non-zero elements.
#Time complexity: O(n)
#space complexity: O(1)
def movezerostoend(nums):
    if len(nums)==0:
        return nums
    i=0
    for i in range(len(nums)):
        if nums[i]==0:
            break
        i+=1
    if i==len(nums):
        return nums
    j=i+1
    while j<len(nums):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
        j+=1
    return nums
