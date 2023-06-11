# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return mergeSort(head)
        
def mergeSort(head):
    # Base case: if the list is empty or contains only one node
    if head is None or head.next is None:
        return head

    # Split the linked list into two halves
    mid = getMiddle(head)
    mid_next = mid.next
    mid.next = None

    # Recursive sort on the two halves
    left = mergeSort(head)
    right = mergeSort(mid_next)

    # Merge the sorted halves
    sorted_list = merge(left, right)

    return sorted_list

def merge(left, right):
    # Create a dummy node as the head of the merged list
    dummy = ListNode(0)
    tail = dummy

    # Merge the two sorted linked lists
    while left and right:
        if left.val < right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    # Attach the remaining nodes, if any
    if left:
        tail.next = left
    if right:
        tail.next = right

    return dummy.next

def getMiddle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow