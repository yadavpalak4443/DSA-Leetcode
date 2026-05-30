# Find starting point of cycle in a linked list Leetcode 142
#Approach: Two pointer approach
#Time complexity: O(n)
#Space complexity: O(1)

class Solution(object):
    def detectCycle(self, head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None :
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None
        