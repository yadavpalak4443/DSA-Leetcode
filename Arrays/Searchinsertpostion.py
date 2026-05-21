#Search Insert position Leetcode 35
#Approach: Binary Search
#Algorithm: Binary search is an efficent algorithm for finding an item from a sorted list of items. 
# it works by repeatedly dividing in half the portion of the list that can contain the item
#Time complexity: O(log n)
#Space complexity: O(1)

def searchInsert(self, nums, target):
    n = len(nums)
    lb = n
    low = 0
    high = n - 1
    while low <= high:
        mid=(low+high)//2
        if nums[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    return lb