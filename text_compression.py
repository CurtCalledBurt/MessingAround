class Leaf():
    def __init__(self):
        self.char = None
        self.count = 0
        self.left = None
        self.right = None


# encode text
# breadth first search seems like the option to use here?
def encode_char(char_we_seek, start_leaf):
    encoding = ""
    qq = []
    qq.append((start_leaf, encoding))
    while len(qq) > 0:
        node = qq.pop()
        leaf = node[0]
        encoding_so_far = node[1]
        if leaf.char == char_we_seek:
            return encoding_so_far
        else:
            if leaf.left:
                qq.append((leaf.left, encoding_so_far + "0"))
            if leaf.right:
                qq.append((leaf.right, encoding_so_far + "1"))


def encode_string(text):
    # count all the characters
    counts = {}
    for char in text:
        if char not in counts.keys():
            counts[char] = 1
        else:
            counts[char] += 1

    # create the queue
    queue = []
    for char in counts.keys():
        node = Leaf()
        node.char = char
        node.count = counts[char]
        queue.append(node)

    # sort the queue based on count
    queue.sort(key=lambda x: -x.count) # the "-" causes sort from highest count to lowest, as desired

    # create the tree
    while len(queue) > 1:
        # get last 2 elements
        node_1 = queue[-1]
        node_2 = queue[-2]
        # add elements to new leaf node
        node = Leaf()
        node.count = node_1.count + node_2.count
        node.left = node_1
        node.right = node_2
        # add new node to queue, delete old nodes
        queue.pop(-1)
        queue.pop(-1)
        queue.append(node)
        # sort node back into queue
        queue.sort(key=lambda x: -x.count)

    tree = queue[0]

    encoding = ""
    for char in text:
        encoding += encode_char(char, tree)
    
    return tree, encoding


def decode_string(tree, encoded_string):
    # decode text
    decoded_string = ""
    node = tree
    for bit in encoded_string:
        # go left or right
        if bit == "0":
            node = node.left
        elif bit == "1":
            node = node.right
        # if we've hit a letter, add it to decode string
        if node.char:
            decoded_string += node.char
            node = tree

    return decoded_string



text = "This is a thing to decode."
print("\n", text)

tree, encoded = encode_string(text)
print(encoded)
print("bits original text takes up: ", len(text)*8)
print("bits encoded text takes up: ", len(encoded))

print(decode_string(tree, encoded), "\n")