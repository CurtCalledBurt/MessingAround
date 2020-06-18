# Node class
class Node():
    def __init__(self, value=None):
        self.next = None
        self.value = value

# create linked list
head_node = Node(0)
current = head_node
for i in range(1,5):
    current.next = Node(i)
    current = current.next

# print values of linked list
# current = head_node
# while current:
#     print(current.value)
#     current = current.next

# reverse a linked list
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


# print reversed linked list
current = new_head
while current:
    print(current.value)
    current = current.next
