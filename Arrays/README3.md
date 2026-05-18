Maximum Subarray — LeetCode
Approach

Used Kadane's Algorithm.

First, take a variable max_sum and initialize it with nums[0].
Take another variable total to store the current subarray sum.
Traverse the array.
Add each element to total.
Update max_sum by comparing max_sum and total.
If total < 0, reset total = 0 because a negative sum cannot help in getting a maximum subarray sum.
Finally, return max_sum.
Time Complexity
O(n)

Because we traverse the array only one time.

Space Complexity
O(1)

Because we use only two extra variables.