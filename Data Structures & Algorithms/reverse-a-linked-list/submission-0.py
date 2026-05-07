# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
            
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        for i in range(length // 2):
            
            left_node = head
            for _ in range(i):
                left_node = left_node.next
                
            right_node = head
            for _ in range(length - 1 - i):
                right_node = right_node.next
            
            left_node.val, right_node.val = right_node.val, left_node.val
            
        return head


        