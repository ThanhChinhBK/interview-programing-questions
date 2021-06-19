# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes_length = 0
        curr = head
        while curr != None:
            nodes_length += 1
            curr = curr.next
        deleted_num = nodes_length - n
        if deleted_num == 0:
            return head.next
        curr_num = 1
        curr_node = head
        while curr_num < deleted_num:
            curr_node = curr_node.next
            curr_num += 1
        if curr_node != None and curr_node.next != None:
            curr_node.next = curr_node.next.next
        return head
