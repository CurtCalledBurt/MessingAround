# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def add_two_numbers(ListNodeA, ListNodeB):
    # extract digits of each number contained in the lists and convert them to a string, then to an integer
    current = ListNodeA
    numA = ""
    while current:
        numA = f"{current.val}" + numA
        current = current.next
    numA = int(numA)

    current = ListNodeB
    numB = ""
    while current:
        numB = f"{current.val}" + numB
        current = current.next
    numB = int(numB)

    total = numA + numB
    total = str(total)

    # runs through 'total' converting it into a LinkedList
    head = ListNode(int(total[-1]))
    current = head
    # starts iteration at the second to last character in 'total', and works its way back to the first character, creating a ListNode connected to the previous node for each character
    for i in range(len(total) - 2, -1, -1):
        current.next = ListNode(int(total[i]))
        current = current.next

    return head


# Helper code that creates a linked list from an array of numbers
arrayA = [2,4,3]
arrayB = [5,6,4]

headA = ListNode(arrayA[0])
head = headA
for i in range(1, len(arrayA)):
    head.next = ListNode(arrayA[i])
    head = head.next

headB = ListNode(arrayB[0])
head = headB
for i in range(1, len(arrayB)):
    head.next = ListNode(arrayB[i])
    head = head.next

# test the function
head = add_two_numbers(headA, headB)
print(head)
current = head
while current:
    print(current.val)
    current = current.next

        