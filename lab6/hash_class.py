class HashTable:
    def __init__(self):
        self.m = 2000003
        self.table = [None] * self.m

    def h1(self, x):
        return abs(x) % self.m

    def h2(self, x):
        return 1 + (abs(x) % (self.m - 1))

    def hash_func(self, x, k):
        return (self.h1(x) + k * self.h2(x)) % self.m

    def _search(self, x):
        i = 0
        first_deleted = -1
        while i < self.m:
            j = self.hash_func(x, i)
            if self.table[j] == x:
                return j, True
            elif self.table[j] is None:
                return first_deleted if first_deleted != -1 else j, False
            elif self.table[j] == 'DELETED' and first_deleted == -1:
                first_deleted = j
            i += 1
        return first_deleted if first_deleted != -1 else -1, False

    def insert(self, x):
        j, exist = self._search(x)
        if exist:
            return
        if j == -1:  # Переполнение
            raise OverflowError
        self.table[j] = x

    def remove(self, x):
        j, exist = self._search(x)
        if exist:
            self.table[j] = 'DELETED'

    def contains(self, x):
        _, exist = self._search(x)
        return 'Y' if exist else 'N'


class HashTupleTable(HashTable):
    def __init__(self):
        super().__init__()

    def _search(self, x):
        i = 0
        first_deleted = -1
        while i < self.m:
            j = self.hash_func(x, i)
            if self.table[j] is None:
                return first_deleted if first_deleted != -1 else j, False
            elif self.table[j][0] == x:
                return j, True
            elif self.table[j] == 'DELETED' and first_deleted == -1:
                first_deleted = j
            i += 1
        return first_deleted if first_deleted != -1 else -1, False

    def insert(self, x):
        number, name = x
        j, exist = self._search(number)
        if j == -1:  # Переполнение
            raise OverflowError
        self.table[j] = (number, name)

    def remove(self, number):
        j, exist = self._search(number)
        if exist:
            self.table[j] = 'DELETED'

    def contains(self, number):
        j, exist = self._search(number)
        if exist:
            _, name = self.table[j]
            return name
        return 'not found'


class Node:
    def __init__(self, key, value):
        self.prev = None
        self.key = key
        self.value = value
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def pop(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

class HashListTable:
    def __init__(self):
        self.m = 4000001
        self.table = [None] * self.m
        self.dll = DoubleLinkedList()

    def h1(self, key):
        p, m = 31, self.m
        h = 0
        for c in key:
            h = (h * p + ord(c))
        return h % m

    def hash_func(self, x, k):
        return (self.h1(x) + k * 37) % self.m

    def _search(self, key):
        i = 0
        first_deleted = -1
        while i < 100:
            j = self.hash_func(key, i)
            if self.table[j] is None:
                return first_deleted if first_deleted != -1 else j, False
            if isinstance(self.table[j], Node) and self.table[j].key == key:
                return j, True
            elif self.table[j] == 'DELETED' and first_deleted == -1:
                first_deleted = j
            i += 1
        return first_deleted if first_deleted != -1 else -1, False

    def insert(self, x):
        key, val = x
        j, exist = self._search(key)
        if j == -1:  # Переполнение
            raise OverflowError
        if exist:
            self.table[j].value = val
        else:
            self.table[j] = Node(key, val)
            self.dll.append(self.table[j])

    def remove(self, key):
        j, exist = self._search(key)
        if exist:
            self.dll.pop(self.table[j])
            self.table[j] = 'DELETED'

    def get(self, x):
        j, exist = self._search(x)
        return self.table[j].value if exist else '<none>'

    def prev(self, x):
        j, exist = self._search(x)
        if exist:
            node = self.table[j]
            prev_node = node.prev
            return prev_node.value if prev_node and prev_node.key else '<none>'
        return '<none>'

    def next(self, x):
        j, exist = self._search(x)
        if exist:
            node = self.table[j]
            next_node = node.next
            return next_node.value if next_node and next_node.key else '<none>'
        return '<none>'