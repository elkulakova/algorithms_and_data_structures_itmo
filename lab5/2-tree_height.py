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


def get_tree_height(tree, n):
    if tree is None:
        return 0
    for i in range(n-1):
        tree = get_tree_height(tree, i + 1)
        return [tree.index(leaf) for leaf in tree if leaf == i]


if __name__ == "__main__":
    with open('input.txt') as f:
        n = int(f.readline())
        array = list(map(int, f.readline().split()))