# 78. Subsets
# Given an integer array nums of unique elements, return all possible subsets (the power set).
#Algorithm: Bit manipulation
#step1: Calculate the total number of subsets using 2^n, where n is the length of the input array.
#step2: Iterate through the range of total subsets and for each number, determine which elements to include in the current subset by checking the bits of the number.
#time complexity: O(n*2^n) where n is the number of elements in the input array. This is because we are generating 2^n subsets and for each subset, we are iterating through n elements to check if they are included in the subset.
#space complexity: O(n*2^n) since we are storing all the subsets in the result list, and each subset can have up to n elements.
class solution(object):
    def subsets(self,nums):
        n=len(nums)
        total_subsets=1<<n
        result=[]
        for num in range(0,total_subsets):
            lst=[]
            for i in range(0,n):
                if num & (1<<i):
                    lst.append(nums[i])
            result.append(lst)
        return result