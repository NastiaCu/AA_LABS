import random


def unbalanced_tree(num_nodes):
    tree = {'1': set()}

    for i in range(2, num_nodes):
        parent_node = random.choice(list(tree.keys()))
        tree[parent_node].add(str(i))
        tree[str(i)] = set()

    for i in range(num_nodes, 2 * num_nodes):
        parent_node = random.choice(list(tree.keys()))
        tree[parent_node].add(str(i))
        tree[str(i)] = set()
    return tree
