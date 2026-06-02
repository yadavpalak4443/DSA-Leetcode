#Remove duplicates from sorted DLL geeksforgeeks
#Approch: we will traverse the list and check if the current node is same as the previous node if it is then we will remove the current node by changing the next pointer of the previous node and the prev pointer of the next node
#time complexity: O(n) where n is the number of nodes in the linked list.
#space complexity: O(1) since we are using only a constant amount of extra space for the pointers.
class solution:
    def removeDuplicates(self,head):
        if not head:
            return head
        curr=head.next
        while curr:
            if curr.data==curr.prev.data:
                curr.prev.next=curr.next
            if curr.next:
                curr.next.prev=curr.prev
            curr=curr.next
        return head