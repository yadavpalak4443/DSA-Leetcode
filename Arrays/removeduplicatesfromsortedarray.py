# Remove Duplicates from Sorted Array Leetcode 26
# Approach: Two pointers
#Algorithm:
#1. We will maintain two pointers, i and j, where i will keep track of the last unique element and j will iterate through the array.
#2. We will compare the elements at i and j and if they are different , we will increment i and update the element at i to the element at j.
# Time complexity: O(n)
# Space complexity: O(1)



def removeduplicates(nums):
    if len(nums)==1:
        return 1
    i=0
    j=i+1
    while j<len(nums):
        if nums[j]!=nums[i]:
            i+=1
            nums[i],nums[j]=nums[j],nums[i]
        j+=1
    return i+1
    