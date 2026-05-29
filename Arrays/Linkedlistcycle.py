#Linked List cycle leetcode 141
#Approach: Two pointer approach
#Time complexity: O(n)
#Space complexity: O(1)

class solution(object):
    def hascycle(self,head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False