# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        temp = head
        while temp != None:
            temp = temp.next
            length+=1
        r = length - n
        if r == 1:
            return head.next
        else:
            index = 0
            temp = head
            prev = head
            while index != r-1:
                index+=1
                prev = temp
                temp = temp.next
            prev.next = temp.next
        return head
                 
        