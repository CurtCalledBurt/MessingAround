# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# helper function that creates a linked list from an array and returns the head node
def create_linked_list(array):
    head = ListNode(array[0])
    current = head
    for i in range(1, len(array)):
        current.next = ListNode(array[i])
        current = current.next
    return head

# helper function that takes a linked list head and prints all the node values
def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next
    return

# array = [1,2,3,4]
# head = create_linked_list(array)
# print_linked_list(head)

def merge_linked_lists(headA, headB):

    # establish which head node will be the merged list's head node
    currentA = headA
    currentB = headB
    if headA.val <= headB.val:
        current = currentA
        currentA = currentA.next
        head = headA
    else:
        current = currentB
        currentB = currentB.next
        head = headB

    # merge the lists
    while currentA and currentB:
        if currentA.val <= currentB.val:
            current.next = currentA
            currentA = currentA.next
        else:
            current.next = currentB
            currentB = currentB.next
        current = current.next
        
        # when we reach the end of one of the lists, connect the remaining nodes in the other list to the end of our merged list
        if currentA is None:
            while currentB:
                current.next = currentB
                currentB = currentB.next
                current = current.next
        if currentB is None:
            while currentA:
                current.next = currentA
                currentA = currentA.next
                current = current.next
    return head

arrayA = [1,2,4]
arrayB = [1,3,4]

headA = create_linked_list(arrayA)
headB = create_linked_list(arrayB)

final_head = merge_linked_lists(headA, headB)

print_linked_list(final_head)