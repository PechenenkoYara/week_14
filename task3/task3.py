# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left


            min_larger_node = self.get_min(root.right)
            root.val = min_larger_node.val
            root.right = self.deleteNode(root.right, min_larger_node.val)

        return root

    def get_min(self, node):
        while node.left:
            node = node.left
        return node
