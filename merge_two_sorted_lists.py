# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        head = ListNode()

        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2
        return head.next
        # return sorted(list1 + list2)

solution = Solution()

def createLinkedList(lst):
    head = None
    for val in reversed(lst):
        head = ListNode(val, head)
    return head

def toList(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst


obj = Solution()

l1 = createLinkedList([1,2,4])
l2 = createLinkedList([1,3,4])
print(toList(obj.mergeTwoLists(l1, l2)))

l1 = createLinkedList([])
l2 = createLinkedList([])
print(toList(obj.mergeTwoLists(l1,l2)))

l1 = createLinkedList([])
l2 = createLinkedList([0])
print(toList(obj.mergeTwoLists(l1,l2)))

# explanation: https://www.youtube.com/watch?v=E5XXiY6QnAs