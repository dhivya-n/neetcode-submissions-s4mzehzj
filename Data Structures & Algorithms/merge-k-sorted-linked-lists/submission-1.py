# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sys.setrecursionlimit(20000)
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        
        for i in range(1, n):
            lists[i] = self.mergeTwoLists(lists[i-1], lists[i])
        return lists[n-1]

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        newHead = ListNode()
        if list1.val < list2.val:
            newHead.val = list1.val
            newHead.next = self.mergeTwoLists(list1.next, list2)
        else:
            newHead.val = list2.val
            newHead.next = self.mergeTwoLists(list1, list2.next)  
        return  newHead