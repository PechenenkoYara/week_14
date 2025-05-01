class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def in_order(node):
    if node is None:
        return []
    return in_order(node.left) + [node.data] + in_order(node.right)


def pre_order(node):
    if node is None:
        return []
    return [node.data] + pre_order(node.left) + pre_order(node.right)


def post_order(node):
    if node is None:
        return []
    return post_order(node.left) + post_order(node.right) + [node.data]
