#Middle of the linked list leetcode 876
#Approach:Two pointer approach
#Algorithm: 1. Initialize two pointers, slow and fast, to the head of the linked list.
#2. Move the slow pointer one step at a time and the fast pointer two steps at a time.
#3. When the fast pointer reaches the end of the linked list (i.e., it is null or its next is null), the slow pointer will be at the middle node.

#Time complexity: O(n) where n is the number of nodes in the linked list.
#Space complexity: O(1) since we are using only a constant amount of extra space for the pointers.
class solution(object):
    def middleNode(self,head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow