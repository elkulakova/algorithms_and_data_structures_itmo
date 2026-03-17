class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1
        self.maxs = []
        self.max = float('-inf')

    def push(self, item):
        if item >= self.max:
            self.max = item
            self.maxs.append(item)
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped = self.stack[self.top]
            if popped == self.max:
                self.maxs.pop()
                if not self.maxs:
                    self.max = float('-inf')
                else:
                    self.max = self.maxs[-1]
            self.stack[self.top] = None
            self.top -= 1
            return popped

    def is_empty(self) -> bool:
        if self.top == -1:
            return True
        return False

    def __getitem__(self, index):
        return self.stack[index]