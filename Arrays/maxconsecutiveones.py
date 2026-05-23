# Max consecutive ones leetcode 485
#Approach: We will iterate through the array and count the number of consecutive ones. Whenever we encounter a zero, we will compare the current count with the maximum count and reset the count to zero. Finally, we will return the maximum count.
#Time complexity: O(n)
#Space complexity: O(1)

def maxconsecutiveones(nums):
    count=0
    maxcount=0
    for i in range(len(nums)):
        if nums[i]==1:
            count+=1
        else:
            maxcount=max(maxcount,count)
            count=0
    return max(maxcount,count)
 