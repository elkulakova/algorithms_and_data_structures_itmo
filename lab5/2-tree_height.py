from collections import deque

def build_tree(parent):
    n = len(parent)
    children = [[] for _ in range(n)]
    root = -1
    for i in range(n):
        if parent[i] == -1:
            root = i
        else:
            children[parent[i]].append(i)
    return root, children


def get_tree_height(tree):
    if tree is None:
        return 0

    root, children = build_tree(tree)
    if root == -1:
        return 0

    q = deque([root])
    height = 0

    while q:
        level_size = len(q)
        for _ in range(level_size):
            v = q.popleft()
            for child in children[v]:
                q.append(child)
        height += 1

    return height


if __name__ == "__main__":
    with open('input.txt') as f:
        n = int(f.readline())
        array = list(map(int, f.readline().split()))