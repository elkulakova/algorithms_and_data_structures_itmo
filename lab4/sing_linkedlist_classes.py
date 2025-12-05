class Node:
    def __init__(self, value):
        self.key = value
        self.next = None

    def name_neibs(self):
        right_val = self.next.key if self.next else 0
        return right_val


class SingleLinkedList:
    def __init__(self, n):
        self.nodes_list = [None] * (n + 1)
        for i in range(1, n + 1):
            self.nodes_list[i] = Node(i)

        self.head = None
        self.tail = None

    def get_node(self, value):
        return self.nodes_list[value]

    def _in_list(self, node):
        if node is self.head or node is self.tail:
            return True
        cur = self.head
        while cur:
            if cur is node:
                return True
            cur = cur.next
        return False

    def _detach(self, node):
        if not self._in_list(node):
            return

        if node is self.head:
            self.head = node.next
            if self.head is None:
                self.tail = None
            node.next = None
            return

        prev = self.head
        while prev and prev.next is not node:
            prev = prev.next

        if prev is None:
            return

        prev.next = node.next
        if node is self.tail:
            self.tail = prev
        node.next = None


    def show_nodes(self):
        vals = []
        cur = self.head
        while cur:
            vals.append(cur.key)
            cur = cur.next
        return vals

    def find(self, key):
        cur = self.head
        while cur:
            if cur.key == key:
                return cur
            cur = cur.next
        return None

    def add_node_head(self, value):
        node = self.get_node(value)
        if node is self.head:
            return
        if self._in_list(node):
            self._detach(node)

        if self.head is None:
            self.head = self.tail = node
            node.next = None
        else:
            node.next = self.head
            self.head = node

    def remove_node_head(self):
        if not self.head:
            return
        node = self.head
        self.head = node.next
        if self.head is None:
            self.tail = None
        node.next = None

    def add_node_right(self, key_j, key_i):
        node_j = self.find(key_j)
        if node_j is None:
            return

        node_i = self.get_node(key_i)
        if self._in_list(node_i):
            self._detach(node_i)

        node_i.next = node_j.next
        node_j.next = node_i
        if self.tail is node_j:
            self.tail = node_i

    def remove_node_right(self, key_j):
        node_j = self.find(key_j)
        if node_j is None:
            return

        target = node_j.next
        if target is None:
            return

        node_j.next = target.next
        if target is self.tail:
            self.tail = node_j
        target.next = None