# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
"""

def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if not root:
        return False
    if root and not root.left and not root.right and root.val == sum:
        return True
    return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

"""
def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    stack = []
    stack.append((root, 0))
    while stack:
        node, path = stack.pop()
        if not node: continue
        path += node.val
        if not node.left and not node.right and path == sum:
            return True
        if node.left:
            stack.append((node.left, path))
        if node.right:
            stack.append((node.right, path))
    return False
"""