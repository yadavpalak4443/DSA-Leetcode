def maximumsubarray(nums):
    max_sum=nums[0]
    total=0
    for num in nums:
        total+=num
        max_sum=max(max_sum,total)
        if total<0:
            total=0
    return max_sum