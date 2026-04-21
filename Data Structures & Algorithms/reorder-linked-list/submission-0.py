# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        temp = head
        while temp is not None:
            temp = temp.next
            length+=1
        
        half = math.ceil(length/2)
        head1, i = head, 1
        while i != half:
            head = head.next
            i+=1
        list2 = head.next
        head.next = None
        #Reverse the list 2
        prev = None
        while list2 != None:
            dummy = list2.next
            list2.next = prev
            prev = list2
            list2 = dummy
        #Rearrange the links
        head2 = prev
        while head1 != None and head2 != None:
            temp1 = head1.next
            temp2 = head2.next
            head1.next = head2
            head2.next = temp1
            head1 = temp1
            head2 = temp2
        

        