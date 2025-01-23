# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        # initial a newnode and use dummy node to update
        dummy = ListNode()
        head = dummy
        cur_sum = 0
        while l1 or l2 :
            if l1:
                cur_sum = cur_sum+l1.val
                l1 = l1.next
            if l2:
                cur_sum = cur_sum+l2.val
                l2 = l2.next

            # check if need to carry, and assign node
            new_node = ListNode(cur_sum % 10)
            cur_sum = cur_sum // 10

            dummy.next = new_node
            dummy = dummy.next
        # check if remaine val
        if cur_sum  > 0:
            new_node = ListNode(cur_sum)
            dummy.next = new_node
            dummy = dummy.next

        return head.next
      # time complexity: O(N)
      # space complexity: O(N)
