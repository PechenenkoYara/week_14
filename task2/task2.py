        
        
def tree_by_levels(node):
    to_check = [node]
    res = []
    while len(to_check) > 0:
        node = to_check.pop(0)
        if node is None:
            continue
        res.append(node.value)
        to_check.append(node.left)
        to_check.append(node.right)
    return res