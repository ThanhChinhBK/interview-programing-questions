# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        new_head = head
        curr_node = head
        swap = True
        while curr_node != None:
            temp_node = curr_node.next
            if temp_node is not None and swap:
                curr_node.val, temp_node.val = temp_node.val, curr_node.val
            curr_node = temp_node
            swap = !swap
        return head
                
