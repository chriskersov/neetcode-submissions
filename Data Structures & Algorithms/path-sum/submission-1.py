# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.hasPathSumHelper(root, targetSum, 0)
    def hasPathSumHelper(self, root, targetSum, sumSoFar):
        if not root:
            return False
        sumSoFar += root.val
        if not root.left and not root.right:
            if sumSoFar == targetSum:
                return True
        if self.hasPathSumHelper(root.left, targetSum, sumSoFar):
            return True
        if self.hasPathSumHelper(root.right, targetSum, sumSoFar):
            return True
        sumSoFar -= root.val
        return False
        
        