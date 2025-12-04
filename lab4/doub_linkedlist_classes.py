class Node:
    def __init__(self, value):
        self.prev = None
        self.key = value
        self.next = None

    def name_neibs(self):
        left_val = self.prev.key if self.prev else 0
        right_val = self.next.key if self.next else 0
        return left_val, right_val


class DoubleLinkedList:
    def __init__(self, n):
        self.nodes_list = [None] * (n + 1)
        for i in range(1, n + 1):
            self.nodes_list[i] = Node(i)

        self.head = None
        self.tail = None

    def get_node(self, value):
        return self.nodes_list[value]

    def _in_list(self, node):
        # узел считается «в списке», если указывает голова/хвост
        # или у него есть связи prev/next
        if node is self.head or node is self.tail:
            return True
        if node.prev is not None or node.next is not None:
            return True
        return False

    def add_node_left(self, val_j, val_i):
        node_j = self.get_node(val_j)
        node_i = self.get_node(val_i)

        # нельзя вставить слева от узла, которого нет в списке
        if not self._in_list(node_j):
            return

        # если node_i уже в списке — сначала «вырежем» его
        if self._in_list(node_i):
            self._detach(node_i)

        prev_left = node_j.prev
        node_j.prev = node_i
        node_i.next = node_j
        node_i.prev = prev_left
        if prev_left:
            prev_left.next = node_i
        else:
            self.head = node_i

    def _detach(self, node):
        """Вырезать узел из текущего списка, если он в нём есть."""
        if not self._in_list(node):
            return
        left = node.prev
        right = node.next

        if left:
            left.next = right
        else:
            # node был головой
            self.head = right

        if right:
            right.prev = left
        else:
            # node был хвостом
            self.tail = left

        node.prev = node.next = None

    def remove_node_left(self, value):
        node = self.get_node(value)
        if not self._in_list(node):
            return

        left_node = node.prev
        if not left_node:
            return

        left = left_node.prev
        right = left_node.next

        if left:
            left.next = right
        else:
            self.head = right

        if right:
            right.prev = left
        else:
            self.tail = left

        left_node.prev = left_node.next = None

    def add_node_head(self, value):
        node = self.get_node(value)

        # если уже голова — ничего не делаем
        if node is self.head:
            return

        # если узел уже где-то в списке — вырезаем
        if self._in_list(node):
            self._detach(node)

        if self.head is None:
            self.head = self.tail = node
            node.prev = node.next = None
        else:
            prev_head = self.head
            self.head = node
            node.prev = None
            node.next = prev_head
            prev_head.prev = node

    def add_node_tail(self, value):
        node = self.get_node(value)

        # если уже хвост — ничего не делаем
        if node is self.tail:
            return

        if self._in_list(node):
            self._detach(node)

        if self.tail is None:
            self.head = self.tail = node
            node.prev = node.next = None
        else:
            prev_tail = self.tail
            self.tail = node
            node.next = None
            node.prev = prev_tail
            prev_tail.next = node

    def remove_node_head(self):
        if not self.head:
            return
        node = self.head
        self.head = node.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        node.prev = node.next = None

    def remove_node_tail(self):
        if not self.tail:
            return
        node = self.tail
        self.tail = node.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        node.prev = node.next = None

    def show_nodes(self):
        vals = []
        cur = self.head
        while cur:
            vals.append(cur.key)
            cur = cur.next
        return vals
