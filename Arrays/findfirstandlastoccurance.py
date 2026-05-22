#34. Find First and Last Position of Element in Sorted Array
#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#Approach: Binary Search lowerbound and upperbound 
#Time complexity: O(log n)
#space complexity: O(1)
class Solution(object):
    def lowerbound(self,nums,target):
        low=0
        high=len(nums)-1
        ans=len(nums)
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def upperbound(self,nums,target):
        ans=len(nums)
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

    def searchRange(self, nums, target):
        
        first=self.lowerbound(nums,target)
        if first==len(nums) or nums[first]!=target:
            return [-1,-1]
        last=self.upperbound(nums,target)-1
        return [first,last]
        