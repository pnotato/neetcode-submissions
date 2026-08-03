# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            future = curr.next
            curr.next = prev
            prev = curr
            curr = future
        return prev


       
        # prev = head
        # curr = head.next

        # while head.next:
        #     future = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr.next = future

        # return curr
        # self solution. obviously didn't go well.