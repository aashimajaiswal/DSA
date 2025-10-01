# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # create a dummy
        dummy = ListNode()
        current = dummy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # Base case 1: if list1 is empty, return list2
        if not list1:
            return list2
        
        # Base case 2: if list2 is empty, return list1
        if not list2:
            return list1
        
        # Recursive case: pick smaller node and merge rest
        if list1.val <= list2.val:
            # Pick list1's node
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            # Pick list2's node
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        
        # check until for both its null
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # attach remaining
        current.next = list1 if list1 else list2

        return dummy.next
        