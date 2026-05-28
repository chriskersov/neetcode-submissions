# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = self.inOrder(root, [], k)
        return result[k - 1]
    def inOrder(self, root, result, k):
        if not root:
            return result
        self.inOrder(root.left, result, k)
        result.append(root.val)
        if len(result) == k:
            return result
        self.inOrder(root.right, result, k)
        return result
