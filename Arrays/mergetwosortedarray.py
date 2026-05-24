# 88. Merge Sorted Array
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# Time complexity: O(m+n)
# Space complexity: O(m+n) for the result array, but we can optimize it to O(1) by merging in place.
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        result=[]
        i=0
        j=0
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1

        while i<m:
            result.append(nums1[i])
            i+=1
        while j<n:
            result.append(nums2[j])
            j+=1
        for k in range(m + n):
            nums1[k] = result[k]
        