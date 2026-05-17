#Validparentheses Leetcode

#Approach

Used Stack approach.

Push opening brackets into stack.
If closing bracket comes, check top element.
If brackets match, pop from stack.
Otherwise return False.

At the end, if stack becomes empty then parentheses are valid.

Time Complexity

O(n)

Because we traverse the string only one time.

Space Complexity

O(n)

Because in worst case all opening brackets are stored in stack.
