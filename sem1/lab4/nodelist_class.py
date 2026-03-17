class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

    def name_neibs(self):
        left_val = self.prev.value if self.prev else 0
        right_val = self.next.value if self.next else 0
        return left_val, right_val


class NodeList:
    def __init__(self, n):
        self.nodes_list = [None] * (n + 1)
        for i in range(1, n + 1):
            self.nodes_list[i] = Node(i)

        # изначально в строю только 1
        self.head = self.nodes_list[1]
        self.tail = self.head

    def get_node(self, value):
        return self.nodes_list[value]

    def add_node_left(self, val_j, val_i):
        node_j = self.get_node(val_j)
        node_i = self.get_node(val_i)
        prev_left = node_j.prev
        node_j.prev = node_i
        node_i.next = node_j
        node_i.prev = prev_left
        if prev_left:
            prev_left.next = node_i
        else:
            self.head = node_i

    def add_node_right(self, val_j, val_i):
        node_j = self.get_node(val_j)
        node_i = self.get_node(val_i)
        prev_right = node_j.next
        node_j.next = node_i
        node_i.prev = node_j
        node_i.next = prev_right
        if prev_right:
            prev_right.prev = node_i
        else:
            self.tail = node_i

    def remove_node(self, value):
        node = self.get_node(value)
        left = node.prev
        right = node.next

        if left:
            left.next = right
        else:
            self.head = right

        if right:
            right.prev = left
        else:
            self.tail = left

        node.prev = node.next = None

    def name(self, value):
        node = self.get_node(value)
        return node.name_neibs()