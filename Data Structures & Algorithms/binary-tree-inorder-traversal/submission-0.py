# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        return self.inorderHelper(root, result)
    def inorderHelper(self, root, result):
        if not root:
            return result
        self.inorderHelper(root.left, result)
        result.append(root.val)
        self.inorderHelper(root.right, result)
        return result