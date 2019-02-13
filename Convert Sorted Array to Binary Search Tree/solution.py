# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedArrayToBST(nums: 'List[int]') -> 'TreeNode':
    # Time: O(n)
    # Space: O(n)
    def convert(left, right):
        if left > right:
            return None

        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = convert(left, mid - 1)
        root.right = convert(mid + 1, right)

        return root
    
    return convert(0, len(nums) - 1)

def inOrder(node: 'TreeNode') -> 'None':
    if not node:
        return None

    inOrder(node.left)
    print(node.val)
    inOrder(node.right)

arr1 = [-10, -3, 0, 5, 9, 10]
bst1 = sortedArrayToBST(arr1)
inOrder(bst1)