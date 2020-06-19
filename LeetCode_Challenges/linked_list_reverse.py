# Node class
class Node():
    def __init__(self, value=None):
        self.next = None
        self.value = value

# create linked list from an array
def create_linked_list(array):
    head_node = Node(array[0])
    current = head_node
    for i in range(1, len(array)):
        current.next = Node(array[i])
        current = current.next
    return head_node

# print values of nodes in linked list
def print_linked_list(head_node):
    current = head_node
    while current:
        print(current.value)
        current = current.next

array = [1,2,3,4,5]

head_node = create_linked_list(array)

# reverse a linked list
def reverse_linked_list(head_node):
    new_head = head_node
    current = new_head
    prev = None

    while current:
        # save the next node
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
        if current is None:
            new_head = prev
    return new_head

new_head = reverse_linked_list(head_node)

print_linked_list(new_head)
