def balanced_tree(num_nodes):
    tree = {}
    queue = ['1']
    count = 1
    while queue and count < num_nodes:
        parent = queue.pop(0)
        children = set()
        for i in range(3):
            count += 1
            child = str(count)
            children.add(child)
            tree[child] = set()
            queue.append(child)
            if count == num_nodes:
                break
        tree[parent] = children
    return tree
